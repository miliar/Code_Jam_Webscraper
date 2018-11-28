#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>

int n;

int mat[55][55];


struct arr{
    int a[55];

    static int cmp_idx;
    bool operator ==(const arr &that) const {
        return this->a[cmp_idx] == that.a[cmp_idx];
        }
    bool operator <(const arr &that) const {
        return this->a[cmp_idx] < that.a[cmp_idx];
        }
    void fill_big(){
        memset(a, 127, sizeof a);
        }
    };

int arr::cmp_idx;

arr inp[110];

struct rc{
    char rowcol;
    arr a;

    rc(){rowcol = 0;}
    bool done(){return rowcol != 0;}
    bool tryrow(int idx){
        for(int i = 0; i < n; i++)
            if (mat[idx][i] > 0 && mat[idx][i] != a.a[i])
                return false;
        return true;
        }
    bool trycol(int idx){
        for(int i = 0; i < n; i++)
            if (mat[i][idx] > 0 && mat[i][idx] != a.a[i])
                return false;
        return true;
        }
    void setrow(int idx){
        rowcol = 'r';
        for(int i = 0; i < n; i++)
            mat[idx][i] = a.a[i];
        }
    void setcol(int idx){
        rowcol = 'c';
        for(int i = 0; i < n; i++)
            mat[i][idx] = a.a[i];
        }
    };

rc data[55][2];

int main()
{
    int tc;
    std::cin >> tc;
    for(int tn = 1; tn <= tc; tn++){
        std::cin >> n;
        memset(mat, -1, sizeof mat);
        for (int idx = 0; idx < 2*n-1; idx++)
            for (int i = 0; i < n; i++)
                std::cin >> inp[idx].a[i];
        int idx_to_output;
        arr *inpstt = inp + 0;
        arr *inpfin = inp + 2*n-1;
        for(int idx = 0; idx < n; idx++){
            arr::cmp_idx = idx;
            arr *a1 = std::min_element(inpstt, inpfin);
            data[idx][0].a = *a1;
            arr *a2 = std::find(a1 + 1, inpfin, *a1);
            if (a2 == inpfin){
                data[idx][0].setrow(idx);
                data[idx][1].rowcol = 'c';
                idx_to_output = idx;
                }
            else{
                data[idx][1].a = *a2;
                data[idx][0].rowcol = 0;
                data[idx][1].rowcol = 0;
                a2->fill_big();
                }
            a1->fill_big();
            }
        int fnd_tot = 1;
        int fnd_lst = 0;
        int last_both;
        while (fnd_tot < n){
            fnd_lst = 0;
            last_both = -1;
            for(int idx = 0; idx < n; idx++){
                if (data[idx][0].done())
                    continue;
                bool r0 = data[idx][0].tryrow(idx);
                bool c0 = data[idx][0].trycol(idx);
                bool r1 = data[idx][1].tryrow(idx);
                bool c1 = data[idx][1].trycol(idx);
                if (r0 && c0 && r1 && c1){
                    last_both = idx;
                    }
                else if (r0 && !c0 && c1 || r0 && !r1 && c1){
                    data[idx][0].setrow(idx);
                    data[idx][1].setcol(idx);
                    ++fnd_lst;
                    }
                else if (!r0 && c0 && r1 || c0 && r1 && !c1){
                    data[idx][0].setcol(idx);
                    data[idx][1].setrow(idx);
                    ++fnd_lst;
                    }
                else{
                    std::cerr << "Case #" << tn << ":" << "OOPS";
                    exit(1);
                    }
                }
            fnd_tot += fnd_lst;
            if(fnd_lst == 0){
                if (last_both == -1){
                    std::cerr << "Case #" << tn << ":" << "OOPS";
                    exit(1);
                    }
                data[last_both][0].setrow(last_both);
                data[last_both][1].setcol(last_both);
                fnd_tot += 1;
                }
            }
        std::cout << "Case #" << tn << ":";
        for (int i = 0; i < n; i++)
            std::cout << " " << mat[i][idx_to_output];
        std::cout << std::endl;
        }
    return 0;
}
