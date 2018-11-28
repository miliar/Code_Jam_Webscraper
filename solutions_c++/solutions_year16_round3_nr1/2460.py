#include <bits/stdc++.h>
#define LLI long long int
#define LLUI long long unsigned int
#define LD long double
#define MOD 1000000007LL
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define ABS(x) ((x)<0?-(x):(x))
using namespace std;


typedef struct str{
    char A;
    int count;
}str_count;
bool sortByCount(const str_count &lhs, const str_count &rhs) { return lhs.count > rhs.count; }
int main() {
    LLI T,i,j,k;
    cin>>T;
    LLI N, rem=0;
    LLI temp_count=0;
    bool flag_f=false;
    for(i=1;i<=T;i++){
        cin>>N;
        rem =0;
        vector<str_count> str(N);
        cout<<"Case #"<<i<<":"<<" ";
        for(j=0;j<N;j++){
            cin>>str[j].count;
            str[j].A = 'A'+j;
            rem = rem + str[j].count;
        }
        sort(str.begin(), str.end(), sortByCount);
    //  for(j=0;j<N;j++){
    //      cout<<str[j].A<<endl;
    //  }
        while(true) {
            flag_f = false;
            sort(str.begin(), str.end(), sortByCount);
            if(str[0].count ==1){
                temp_count =0;
                for(j=0;j<N;j++){
                    if(str[j].count==1)
                        temp_count ++;
                }
                if(temp_count==3)
                    {
                        cout<<str[0].A;
                        rem --;
                        str[0].count --;
                        flag_f = true;
                        cout<<" ";
                    }
            }
            if (flag_f == false){
                if(str[0].count>str[1].count){
                    cout<<str[0].A;
                    cout<<" ";
                    rem --;
                    str[0].count --;
                } else{
                    cout<<str[0].A<<str[1].A;
                    cout<<" ";
                    rem = rem -2;
                    str[0].count --;
                    str[1].count --;
                }
            }
            if(rem ==0)
                break;
        }
        cout<<endl;
    }
    
    return 0;
}
