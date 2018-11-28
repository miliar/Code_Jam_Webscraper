#include <iostream>
#include <cstdio>
#include <cmath>
#include <queue>
#include <stack>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <deque>
#include <memory.h>
#include <string>
#include <cstring>
#include <regex>

using namespace std;

bool isPalindrom(unsigned long long a){
    vector<int> p;
    while(a){
        p.push_back(a%(unsigned long long)10);
        a/=(unsigned long long)10;
    }
    for(int i = 0; i < p.size(); i++)
        if(p[i] != p[p.size() - 1 - i])
            return false;
    return true;
}

struct LongNum
{
    int A[110];
    int S;
    LongNum(){
        memset(A,0,sizeof(A));
        S = 1;
    }

    bool isPalindrom(){
        for(int i = 0; i < S/2; i++)
            if(A[i] != A[S - i - 1])
                return false;
        return true;
    }

    LongNum operator *(const LongNum &other) const{
        LongNum res;
        for(int i = 0; i < S; i++)
            for(int j = 0; j < other.S; j++)
                res.A[i+j] += A[i] * other.A[j];
        for(int i = 0; i < 2*S; i++)
            if(res.A[i] > 9){
                res.A[i+1] += res.A[i]/10;
                res.A[i] %= 10;
            }
        if(res.A[2*S - 1] != 0)
            res.S = 2*S;
        else
            res.S = 2*S - 1;
        return res;
    }
    void print(){
        for(int i = S - 1; i >= 0; i--)
            putchar(A[i] + '0');
    }
    bool operator<= (const LongNum &other) const{
        if(S != other.S)
            return S < other.S;
        else{
            for(int i = S-1; i >= 0; i--)
                if(A[i] != other.A[i])
                    return A[i] < other.A[i];
        }
        return true;
    }
    bool operator< (const LongNum &other) const{
        if(S != other.S)
            return S < other.S;
        else{
            for(int i = S-1; i >= 0; i--)
                if(A[i] != other.A[i])
                    return A[i] < other.A[i];
        }
        return false;
    }


};

/*
vector< pair<LongNum, LongNum> > numbers;

LongNum form(int digits){
    if(digits == 1){
        LongNum t1;
        LongNum t2;
        LongNum t3;
        t1.A[0] = 1;
        t2.A[0] = 2;
        t3.A[0] = 3;
        LongNum t1_1 = t1*t1;
        LongNum t2_1 = t2*t2;
        LongNum t3_1 = t3*t3;
        numbers.push_back(make_pair(t1,t1_1));
        numbers.push_back(make_pair(t2,t2_1));
        numbers.push_back(make_pair(t3,t3_1));
    }
    else if(digits == 2){
        LongNum t1;
        LongNum t2;
        t1.A[0] = t1.A[1] = 1; t1.S = 2;
        t2.A[0] = t2.A[1] = 2; t2.S = 2;
        LongNum t1_1 = t1 * t1;
        LongNum t2_1 = t2 * t2;
        numbers.push_back(make_pair(t1,t1_1));
        numbers.push_back(make_pair(t2,t2_1));
    }
    else{
        int digitsToPermute = (digits - 2) / 2;
        for(int i = 0; i < (1 << digitsToPermute); i++){
            LongNum res;
            res.S = digits;
            int p = i;

            for(int j = 0; j < digitsToPermute; j++){
                res.A[1+j] = res.A[res.S - 2 - j] = p%2;
                p/=2;
            }
            if(digits % 2 == 1){
                for(int j = 0; j < 3; j++)
                {
                    res.A[res.S / 2] = j;
                    res.A[0] = res.A[res.S - 1] = 1;
                    LongNum res2 = res * res;
                    if(res2.isPalindrom())
                        numbers.push_back(make_pair(res,res2));
                    res.A[0] = res.A[res.S - 1] = 2;
                    res2 = res * res;
                    if(res2.isPalindrom())
                        numbers.push_back(make_pair(res,res2));
                }

            }
            else
            {
                res.A[0] = res.A[res.S - 1] = 1;
                LongNum res2 = res * res;
                if(res2.isPalindrom())
                    numbers.push_back(make_pair(res,res2));
                res.A[0] = res.A[res.S - 1] = 2;
                res2 = res * res;
                if(res2.isPalindrom())
                    numbers.push_back(make_pair(res,res2));
            }
        }
    }
}
*/

vector<LongNum> numbers;

int main()
{
    /*
    for(int i = 1; i <= 50; i++)
        form(i);
    sort(numbers.begin(), numbers.end());
    for(int i = 0; i < numbers.size(); i++)
    {
        numbers[i].first.print();
        putchar(' ');
        numbers[i].second.print();
        putchar('\n');
    }
    printf("%d",numbers.size());*/


    /*
    for(unsigned long long i = 1; i < 4000000000; i++)
        if(isPalindrom(i) && isPalindrom(i * i)){
            palindroms.push_back(i * i);
            cout << i << " " << i*i << endl;
            //printf("%ulld %ulld\n", i, i*i);
        }
    */

    FILE *f = fopen("numbers","r");
    for(int i = 0; i < 41551; i++)
    {
        char s[110];
        fscanf(f,"%s",s);
        fscanf(f,"%s",s);
        int len = strlen(s);
        LongNum N;
        N.S = len;
        for(int i = 0; i < len; i++)
            N.A[i] = s[len - 1 - i] - '0';
        numbers.push_back(N);
    }
    /*
    for(int i = 0; i < numbers.size(); i++)
    {
        numbers[i].print();
        putchar(' ');
    }
    */
    sort(numbers.begin(), numbers.end());

    freopen("C-large-2.in","r",stdin);
    freopen("C.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int z = 0; z < T; z++){
        printf("Case #%d: ",z+1);
        char As[110], Bs[110];
        scanf("%s%s",As,Bs);

        int len = strlen(As);
        LongNum A;
        A.S = len;
        for(int i = 0; i < len; i++)
            A.A[i] = As[len - 1 - i] - '0';

        len = strlen(Bs);
        LongNum B;
        B.S = len;
        for(int i = 0; i < len; i++)
            B.A[i] = Bs[len - 1 - i] - '0';


        int k = 0;
        for(int i = 0; i < numbers.size(); i++)
            if((numbers[i] <= B) && (A <= numbers[i])){
                //printf("%lld ",palindroms[i]);
                k++;
            }
        printf("%d",k);
        printf("\n");
    }
    return 0;
}

