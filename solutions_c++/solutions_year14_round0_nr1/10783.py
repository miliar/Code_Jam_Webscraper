#include<iostream>
#include<stdlib.h>
#include<algorithm>
#include<vector>

using namespace std;

int main ()
{
    int t;
    cin>>t;
    for ( short k = 1; k <= t ; k++ )
    {
    int r1,r2,temp;
    cin>>r1;
    short a[4],b[4];
    vector<int> ans;
    for ( short i = 0; i < 4 ; i++ )
        for ( short j = 0; j < 4 ; j++)
            {
            if ( i == r1-1 )
                cin>>a[j];
            else
                cin>>temp;
            }
    cin>>r2;
    for ( short i = 0; i < 4 ; i++ )
        for ( short j = 0; j < 4 ; j++)
            {
            if ( i == r2-1 )
                cin>>b[j];
            else
                cin>>temp;
            }
    sort(a, a+4);
    sort(b, b+4);
    int i = 0, j = 0;
    while( i < 4 && j < 4)
    {
           if(a[i] < b[j])
           i++;
           else if(b[j] < a[i])
           j++;
           else /* if arr1[i] == arr2[j] */
           {
                ans.push_back(b[j++]);
                i++;
           }
    }        
    printf("Case #%d: ",k);
    if(ans.size()==1)
    cout<<ans[0]<<endl;
    else if(ans.size()> 1)
    cout<<"Bad magician!"<<endl;
    else
    cout<<"Volunteer cheated!"<<endl;
    }
    //system("pause");
    return 0;
}
