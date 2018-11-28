#include<iostream>
#include<string>

using namespace std;

int main(){
int t;
cin>>t;
int z=1;
while(t--){
    int n;
    cin>>n;
    char s[n+1];
    int sy[n+1];
    cin>>s;
    for(int i=0;i<=n;i++)
        {sy[i]=s[i]-'0';
       //  cout<<sy[i]<<" ";
        }
    int curr_ppl=0,add=0;
    for(int i=0;i<=n;i++){
        if(curr_ppl>=i)
            curr_ppl+=sy[i];
        else{
            add+=i-curr_ppl;
            curr_ppl+=i-curr_ppl;
            curr_ppl+=sy[i];
        }
    }
   cout<<"Case #"<<z<<": "<<add<<endl;
   z++;
}

return 0;
}
