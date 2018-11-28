#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
using namespace std;
int main(int argc, const char * argv[])
{
    freopen("A.in","rt",stdin);
	freopen("A.out","wt",stdout);

    int tn,srn,srn1,arr[4][4],arr1[4][4],result,resultvalue;
    cin>>tn;
    for(int i=0;i<tn;i++)
    {
        result=-1,resultvalue=0;
        cin>>srn;
       // cout<<"srn"<<srn<<"\n";
        for (int j=0; j<4; j++) {
            for (int k=0; k<4; k++) {
                cin>>arr[j][k];
            }
        }
        cin>>srn1;
        //cout<<"srn1"<<srn1<<"\n";
        for (int j=0; j<4; j++) {
            for (int k=0; k<4; k++) {
                cin>>arr1[j][k];
            }
        }
        for (int m=0; m<4; m++) {
            for (int n=0; n<4; n++) {
                //cout<<"comparing"<<arr[srn][m]<<"&"<<arr1[srn1][n]<<"n";
                if(arr[srn-1][m]==arr1[srn1-1][n])
                {
                    
                    result++;
                    resultvalue=arr[srn-1][m];
                }
                
            }
        }
        if (result==-1) {
            cout<<"Case #"<<i+1<<": Volunteer cheated!";
        }
        else if (result>0) {
            cout<<"Case #"<<i+1<<": Bad magician!";
        }
        else
        {
            cout<<"Case #"<<i+1<<": "<<resultvalue;
        }
        if(i<(tn-1))
        cout<<endl;
        
    }
    
    
    
    
    return 0;
}

