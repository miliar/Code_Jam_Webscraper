#include<bits/stdc++.h>
#define ll long long
using namespace std;
 
int main()
{
    ll T,len;
    char str[1000],a;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        ll cnt=0;
        ll ans=0;
        scanf("%s",str);
		len=strlen(str);
        if(len==1 && str[0]=='-'){
            cout << "Case #" << t << ": " <<1<< endl;
            continue;
        }
        else if(len==1 && str[0]=='+'){
            cout << "Case #" << t << ": " <<0<< endl;
            continue;
        }
        a=str[0];
        for(int k=1;str[k]!='\0';k++){
            if(a!=str[k]){
                a=str[k];
                cnt++;
            }
        }
        if((cnt==0 && str[0]=='+') || (str[0]=='-' && cnt==1)){
                if(cnt==0){
                    cout << "Case #" << t << ": " <<0<< endl;
                }
                else if(cnt==1){
                    cout << "Case #" << t << ": " <<1<< endl;
                }
        }
        else{
			a=str[0];
			for(int j=1;str[j]!='\0';j++)
			{
				if(a!=str[j]){
                a=str[j];
                ans++;
				}
			}
			if(str[len-1]=='-')
				cout << "Case #" << t << ": " <<(ans+1)<< endl;
			else if(str[len-1]=='+')
				cout << "Case #" << t << ": " <<ans<< endl;
        }
    }
    return 0;
}