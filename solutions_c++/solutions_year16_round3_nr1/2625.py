#include <iostream>
#include <cstdio>
#include <set>
using namespace std;

int main()
{
    int t,n,temp,a,b,po,clock,safe;
    char res[26] = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
    freopen("in5.in","r",stdin);
    freopen("ans5.txt","w",stdout);
    float num[26],sum,major;
    cin>>t;
    for(int i = 1 ; i <= t ; ++i)
    {
        cout<<"Case #"<<i<<": ";
        sum = 0.0;

        clock = 0;
        cin>>n;
        for(int j = 0 ; j < n ; ++j)
        {
            cin>>num[j];
            sum += num[j];

        }
        major = sum/2.0;

        while(sum != 0)
        {
            clock = 0;
            safe= 0;
            for(int k = 0 ; k < n ; ++k)
            {
                if(num[k] > major && clock == 0)
                {
                    cout<<res[k];
                    num[k]--;
                    --sum;
                    ++safe;
                    clock = 1;
                    break;
                }

            }
            major = sum/2.0;
            for(int k = 0 ; k < n ; ++k)
            {
                if(num[k] > major && clock == 1)
                {
                    cout<<res[k];
                    num[k]--;
                    --sum;
                    ++safe;
                    clock = 0;
                    break;
                }

            }
            if(safe==0)
            {
                int large = 0,save;
                for(int k = 0 ; k < n ; ++k)
                {
                    if(num[k] >large )
                    {
                        save = k;
                        large = num[k];

                /*        cout<<"3"<<res[k];
                        num[k]--;
                        --sum;
                        ++safe;
                        clock = 1;
                        continue;*/
                    }
                }
                cout<<res[save];

                num[save]--;
                sum--;
                ++safe;
                major = sum/2.0;
                for(int k= 0 ; k < n ;  ++k)
                {
                    if(num[k] > major)
                    {
                        cout<<res[k];
                        num[k]--;
                        sum--;
                        break;
                    }
                }

            }
            major = sum/2;

            cout<<" ";
            clock = 0;
        }
        cout<<endl;

    }
    return 0;
}
