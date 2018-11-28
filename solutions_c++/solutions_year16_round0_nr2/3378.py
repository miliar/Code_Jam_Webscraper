#include<bits/stdc++.h>
#define lli long long
using namespace std;
int main()
{
    lli t,n,i,numbers=0,calcsarr[109],nums3,nums1,nums2,ress1;
    string strs1;
    cin>>t;
    getchar();
    while(t--)
    {
        getline(cin,strs1);
        nums3=strs1.size();
        ress1=0;
        for(i=0; i<nums3; i++)
        {
            if(strs1[i]=='+')
            calcsarr[i]=1;
            else 
            calcsarr[i]=0;
        }
        for(nums2=nums3-1; nums2>=0; nums2--)
        {
            if(calcsarr[nums2]==0)
            {
                ress1++;
                for(nums1=nums2; nums1>=0; nums1--)
                {
                    if(calcsarr[nums1]==1)
                        calcsarr[nums1]=0;
                    else
                    calcsarr[nums1]=1;
                }
                for(i=0;i<=nums2;i++)
                    swap(calcsarr[i],calcsarr[nums2-i]);
            }

        }
        strs1.clear();
        cout<<"Case #"<<++numbers<<": "<<ress1<<endl;
    }
	return 0;
}
