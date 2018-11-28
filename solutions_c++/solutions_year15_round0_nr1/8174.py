#include <iostream>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for(int z=1;z<=t;z++)
    {
        int n;
        string s;
        cin >> n >> s;
        int ans=0;
        int temp=0;
        for (int i=0;i<=n;i++)
        {
            if(i>temp && s[i]>'0'){
               int k=i-temp;ans=ans+k;temp=temp+k;}
                
                int k =(int)s[i]-48;

            temp+=k;
        }

        cout << "Case #" << z << ": "  << ans << endl;
    }


}
