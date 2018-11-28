#include <iostream>
#include <algorithm>
#include <sstream>
#include<math.h>
#include<stdio.h>

using namespace std;

int binsrch(int array[],int num, int left,int  right)
{
    int middle;
    while (left < right) {
        middle = left + (right - left) / 2;
        if (array[middle] < num)
            left = middle + 1;
        else
            right = middle;
    }
    return left;
}
int main( )
{
    string lStr;
    long long num,count=0,i,t,p,q,l,h,j,k;

    long long a[]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001LL,102030201LL,104060401LL,121242121LL,123454321LL,125686521LL,400080004LL,404090404LL,10000200001LL,10221412201LL,12102420121LL,12345654321LL,40000800004LL,1000002000001LL,1002003002001LL,1004006004001LL,1020304030201LL,1022325232201LL,1024348434201LL,1210024200121LL,1212225222121LL,1214428244121LL,1232346432321LL,1234567654321LL,4000008000004LL,4004009004004LL};
   

    /*for (long long  lIter = 1; lIter <= 10000000; ++lIter ) {
         stringstream lStrS;
    lStrS << lIter;
    lStr = lStrS.str();

    string lRevStr = lStr;
    reverse( lRevStr.begin(), lRevStr.end() );

    if ( lRevStr == lStr ) {
        //cout << lStr << endl;
        
        stringstream ss;
        ss << lStr;
        ss>>num; //convert string into int and store it in "asInt"
        ss.str(""); //clear the stringstream
        ss.clear(); //clear error flags because "42" is not a valid stream (?)
        k= num*num;

        
        
            stringstream lStrS;
            lStrS << k;
            lStr = lStrS.str();

            string lRevStr = lStr;
            reverse( lRevStr.begin(), lRevStr.end() );
            if ( lRevStr == lStr )
            {
                a[count]=k;
                cout << k << endl;
                count++;
            }
        

    }
    }
*/
    
    cin >> t;
    for(j=1;j<=t;j++)
    {
        cin >> p >> q;

        count=0;
        i=0;
        while(a[i]<=q)
        {
            if(a[i] >= p && a[i]<=q)
            count++;
            i++;
        }
        printf("Case #%lld: %lld\n",j,count);
        
    }

 }

