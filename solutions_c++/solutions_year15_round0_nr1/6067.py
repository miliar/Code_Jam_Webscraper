#include<iostream>
#include<cstdlib>

using namespace std;
int main () {
    long long int t,num,i,count=0,j=1,incr;
    int val;
    long long int sum[10000];
    string str;
    char c;
    cin>>t;

    while(t){
        t-=1;
        count=0;
        cin>>num;
        cin>>str;
        if(str[0]=='0'){
            sum[0]=1;
            count++;
        }
        else{
            val=(int)str[0]-(int)48;
            sum[0]=val;
        }
        for(i=1;i<=num;i++){
            if(str[i]!='0'){
                if(sum[i-1]>=i)
                {
                    val=(int)str[i]-(int)48;
                    sum[i]=sum[i-1]+val;
                }
                else{
                    incr=i-sum[i-1];
                    count+=incr;
                    val=(int)str[i]-(int)48;
                    sum[i]=sum[i-1]+val+incr;
                }
            }
            else{
                sum[i]=sum[i-1];
            }
        }

        cout<<"Case #"<<j<<": "<<count<<endl;
        j++;
    }
    return 0;
}

