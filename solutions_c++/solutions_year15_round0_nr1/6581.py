#include <iostream>
using namespace std;

int main() {
	int t,n,pos=1;
    char str[1000];
    cin>>t;

    while(t--)
   {
   cin>>n;
   cin>>str;
   int ans=0,pre=str[0]-'0';
   for(int i=1;str[i]!='\0';i++)
      {
       if(pre<i)
          {
          int temp=i-pre;
          ans=ans+temp;
          pre=pre+temp+str[i]-'0';
           }
       else
          pre=pre+str[i]-'0';
      }
    cout<<"Case #"<<pos<<": "<<ans<<"\n";
    pos++;
   }

	return 0;
}
