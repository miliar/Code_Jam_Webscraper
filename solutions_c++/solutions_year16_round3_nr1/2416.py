#include <iostream>
using namespace std;

int p[27]={0}, sum, n, totalalive;

int check(int i, int j){

    p[i] -= 1;
    p[j] -= 1;
    sum -=  2;
    if(p[i]<0 || p[j]<0){
        sum += 2;
        p[j] += 1;
        p[i] += 1;
        return 0;
    }

    for(int k=0;k<n;k++){
        if(p[k]*2 > sum){
                p[i] += 1;
                p[j] += 1;
                sum  += 2;
            //cout << p[k];
            return 0;
        }
    }
    sum += 2;
    p[j] += 1;
    p[i] += 1;
    return 1;
}

void eva(){
    if(sum ==3){
        if(totalalive==2){
            for(int i=0;i<n;i++){
                for(int j=i+1;j<n;j++){
                    if(p[i]==2 && p[j]==1){
                        printf("%c %c%c", i+65, i+65,j+65);
                        sum =0;
                        totalalive = 0;
                    }
                }
            }

        }else{
            int record[3]={0}, r=0;
            for(int i=0;i<n;i++){
                if(p[i]==1){
                    record[r] = i;
                    r++;
                }
            }
            printf("%c %c%c", record[0]+65, record[1]+65, record[2]+65);
            sum = 0;
        }

    }else{
        int flag = 0;
        for(int i=0;i<n;i++){
            for(int j=i;j<n;j++){
                //cout << check(i, j) << i << j << endl;
                if(check(i, j)==1){
                    p[i]--;
                    flag = 1;
                    sum--;
                    printf("%c", i+65);
                    p[j]--;
                    sum--;
                    printf("%c", j+65);
                    //for(int k=0;k<n;k++)
                      //  cout << p[k];

                }
                if(flag==1){
                    cout << " ";
                    return;
                }
            }
        }
    }
}

int main(){
    freopen("AA.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for(int i=0;i<t;i++){
        int times = 0;
        cin >> n;
        sum = 0;
        totalalive = n;
        for(int j=0;j<n;j++){
            cin >> p[j];
            sum += p[j];
        }
        cout << "Case #" << i + 1 << ": ";
        while(sum>0){
            eva();
            totalalive = 0;
            for(int j=0;j<n;j++){
                if(p[j]>0)
                    totalalive++;
            }
            //cout << "totalalive" <<totalalive;
        }
        cout << endl;

    }

    return 0;
}
