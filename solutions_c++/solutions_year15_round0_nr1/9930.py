#include <iostream>
#include <algorithm>
#include <fstream>
using namespace std;
int main()
{
    int t,num,cnt,sum,cust=1;
    string s;
    freopen("A-small-attempt1.in","r",stdin);
    freopen("output_file_name.out","w",stdout);
    cin>>t;

    while(t--){

        cin>>num>>s;
        cnt=sum=0;

        sum+=(s[0]-'0');
        for(int i=1 ;i<(int)s.size(); i++){

        if(s[i]!='0'){
            if(sum<i){
                cnt+=(i-sum);
                sum+=(i-sum);
                sum+=(s[i]-'0');
            }
            else{
                sum+=(s[i]-'0');
            }
          }
        }
        cout<<"Case #"<<cust<<": "<<cnt<<endl;
        cust++;
    }

    return 0;
}
