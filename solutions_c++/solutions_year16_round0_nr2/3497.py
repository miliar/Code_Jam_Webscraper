#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    char str[10000];
    char tmp[10000];
    getchar();
    for(int cs=1;cs<=t;cs++){
        gets(str);
        int e;
        int len=strlen(str);
        int i;
        for(i=len-1;i>=0;i--){
            if(str[i]=='-') {e=i+1;break;}
        }
        if(i==-1) e=0;
        //cout<<e<<endl;
        int cnt=0;
        while(e!=0){
            if(str[0]=='-'){
                for(int i=0,j=e-1;i<e;i++,j--){
                    if(str[j]=='-') tmp[i]='+';
                    else tmp[i]='-';
                }
                cnt++;
                for(int i=0;i<e;i++) str[i]=tmp[i];
                //cout<<str[i];
                //cout<<endl;
                for(i=e-1;i>=0;i--){
                    if(str[i]=='-') {e=i+1;break;}
                }
                if(i==-1) e=0;
                //cout<<e<<endl;
            }
            else if(str[0]=='+'){
                for(int i=e-1;i>=0;i--){
                    if(str[i]=='+') {
                            int temp=i;
                        for(int j=0;j<=temp;j++,i--){
                            if(str[i]=='-') tmp[j]='+';
                            else tmp[j]='-';
                        }
                        for(int j=0;j<=temp;j++) str[j]=tmp[j];
                        cnt++;
                        break;
                    }
                }
            }
        }
        printf("Case #%d: %d\n",cs,cnt);
    }
    return 0;
}
