//#include <iostream>
//#include <string.h>
//#include <stdio.h>
//
//using namespace std;
//
//int a[1010];
//char s[1010];
//int main()
//{
//    int T,Smax;
//    int cas=0;
//   // cin>>T;
//   // while(T--)
//  {
//
//        cas++;
//        cin>>Smax;
//        cin>>s;
//        for(int i=0;i<=Smax;i++) a[i]=s[i]-'0';
//        int ans=0;
//        int cot=0;
//        for(int i=0;i<=Smax;i++)
//        {
//            ans=max(ans,i-cot);
//            cot+=a[i];
//        }
//        cout<<"Case #"<<cas<<":"<<" ";
//        cout<<ans<<endl;
//    }
//    return 0;
//}
#include <iostream>
#include <string.h>
#include <stdio.h>
using namespace std;

int a[1010];
char s[1010];
int main()
{
    int T,Smax;
    int cas=0;
while(cin>>s)
  {
//      cout<<"s="<<s<<endl;

        cas++;
        Smax=strlen(s)-1;
        for(int i=0;i<=Smax;i++) a[i]=s[i]-'0';
        int ans=0;
        int cot=0;
        for(int i=0;i<=Smax;i++)
        {
            ans=max(ans,i-cot);
            cot+=a[i];
        }
        cout<<"Case #"<<cas<<":"<<" ";
        cout<<ans<<endl;
    }
    return 0;
}
