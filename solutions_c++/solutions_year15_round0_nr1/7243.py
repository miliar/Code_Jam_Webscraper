/* freopen("input_file_name.in","r",stdin);
freopen("output_file_name.out","w",stdout); */
#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int t, temp;
    cin>>t;
    temp=t;
    while(t--){
        int smax;
        char s[1002];
        cin>>smax;
        scanf("%s", s);
        cout<<"Case #"<<temp-t<<": ";
        long int sum=0, frnd=0;
        sum=(int)(s[0]-'0');
        for(int i=1; i<=smax; i++)
        {
            if(i>sum+frnd)
                frnd+=i-sum-frnd;
            int n=(int)(s[i]-'0');
            sum+=n;
        }
        cout<<frnd;
        cout<<endl;
    }
    return 0;
}
