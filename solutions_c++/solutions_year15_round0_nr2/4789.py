#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<fstream>
#include<utility>
using namespace std;

int Size,arr[1003];
int Fsize,frr[1003];
bool func(int special,int mid)
{
    //printf("sp and mid are %d %d\n",special,mid);
    Fsize=0;
    for(int i=1; i<=Size; i++)
    {
        if(arr[i]<=mid)
        {
            //ok...all pancakes can be finished within "mid" minutes
        }
        else if(arr[i]>mid)
        {
            //To be transferred
            int diff=arr[i]-mid;
            Fsize++;
            frr[Fsize]=diff;
            //printf("pushing %d\n",diff);
        }
    }
    int idx=1;
    while( idx<=Fsize )
    {
        if(frr[idx]>0 && special==0)
        {
            return false;
        }
        if(mid>=frr[idx])
        {
            idx++;
            special--;
            //you have done this part
        }
        else
        {
            frr[idx]-=mid;
            special--;
        }
    }
    return true;
}
int main()
{
    ifstream in;
    ofstream out;
    in.open("B-small-attempt4.in");
    out.open("out.txt");
    int t,D,P,c;
    in>>t;
    c=0;
    for(int cas=1;cas<=t;cas++)
    {
        c++;
        Size=0;
        in>>D;
        for(int i=1; i<=D; i++)
        {
            in>>P;//scanf("%d",&P);
            Size++;
            arr[Size]=P;
        }
        int ans=1000006;
        bool fnd;
        for(int special=0; special<=1000; special++)
        {
            int low=1;
            int up=1000;
            int mid;
            while(low<up)
            {
                mid=low+(up-low)/2;

                //Can mid be my answer ie can we have atmost "mid" non special minutes
                fnd=func(special,mid);
                //printf("special is %d mid is %d and fnd is %d\n",special,mid,fnd);
                if(fnd==false)
                {
                    low=mid+1;
                }
                else
                {
                    up=mid;
                }
            }//EndOfBinarySearch
            //printf("special %d low %d\n",special,low);
            if(special+low<ans)
            {
                ans=special+low;
            }
        }//EndOfSpecialLoop
        out<<"Case #"<<cas<<": "<<ans<<endl;
        //write<<"Case #"<<c<<": "<<ans<<"\n";
    }
    return 0;
}
