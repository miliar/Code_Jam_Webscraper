#include <iostream>
#include <cstdio>
#include <string>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <math.h>

namespace std
{
    template < typename T > std::string to_string( const T& n )
    {
        std::ostringstream stm ;
        stm << n ;
        return stm.str() ;
    }
}

using namespace std;

string compute(string a, string b) {
    int am,bm;
    char ac,bc;
    if(a[0]=='-') {
        am=-1;
        ac=a[1];
    }
    else {
        am=1;
        ac=a[0];
    }
    if(b[0]=='-') {
        bm=-1;
        bc=b[1];
    }
    else {
        bm=1;
        bc=b[0];
    }
    string ansArray[4][4]={"1","i","j","k","i","-1","k","-j","j","-k","-1","i","k","j","-i","-1"};
    int row;
    switch (ac) {
        case '1':
            row=0;
            break;
        case 'i':
            row=1;
            break;
        case 'j':
            row=2;
            break;
        case 'k':
            row=3;
            break;
    }
    int column;
    switch (bc) {
        case '1':
            column=0;
            break;
        case 'i':
            column=1;
            break;
        case 'j':
            column=2;
            break;
        case 'k':
            column=3;
            break;
    }
    string ans = "";
    string ansArr=ansArray[row][column];
    int anm=1;
    ////cout<<ansArr<<" ";
    if(ansArr[0]=='-') {
        anm=-1;
        ansArr.erase(0,1);
    }
    ////cout<<ansArr<<" ";
    if(am*bm*anm==-1)
        ans.append("-");
    ans.append(ansArr);
    return ans;
}

int bsrch(vector<int> a, int b, int n)
{
    int s=0,sz=n;
    int mid=(s+n)/2;
    while(s<=n && mid<sz && mid>=0)
    {
        if(a[mid]==b)
            return 1;
        if(a[mid]>b)
            n=mid-1;
        else
            s=mid+1;
        mid=(s+n)/2;
    }
    return 0;
}

int main()
{
    //freopen("test", "r", stdin);
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    int testCases;
    cin>>testCases;
    for(int testcase=0;testcase<testCases;testcase++)
    {
        int l,m;
        cin>>l>>m;
        //cout<<l<<" "<<m<<endl;
        string a;
        char b;
        for(int i=0;i<l;i++) {
            cin>>b;
            a.append(to_string(b));
        }
        /*for(int i=0;i<l;i++)
            //cout<<a[i];*/
        string c;
        for(int i=0;i<m;i++) {
            c.append(a);
        }
        //for(int i=0;i<c.length();i++)
            //cout<<c[i];
        //cout<<endl;
        //cout<<"done1 ";
        string pre=to_string(c[0]),ans = "NO";
        vector<int> ai;
        vector<int> ak;
        vector<int> a1;
        for(int i=1;i<c.length();i++) {
            if(pre=="i")
                ai.push_back(i);
            else if(pre=="k")
                ak.insert(ak.begin(),i);
            //else if(pre=="1")
            //    a1.push_back(i);
            pre=compute(pre,to_string(c[i]));
        }
        //cout<<"done2 ";
        if(pre!="-1" || ak.size()==0)
            ans="NO";
        else {
            for(int i=0;i<ai.size();i++) {
                //for(int j=0;j<ak.size();j++) {
                    if(ak[0]>ai[i]) {
                        ans="YES";
                        break;
                    }
                    //else
                        //break;
            }
        }
        cout<<"Case #"<<testcase+1<<": "<<ans<<endl;
    }
    return 0;
}
