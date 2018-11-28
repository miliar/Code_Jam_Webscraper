#include<iostream>
#include<string>
#include<map>
#include<vector>
#include<algorithm>
#include<cmath>
#include<climits>
#include<queue>
#include<set>

#define VI vector<int>
#define PII pair<int,int>
#define mp make_pair
#define rep(i,a,b) for(i=(a); i<(b); i++)
#define repI(i,a,b) for(i=(a); i<=(b); i++)

using namespace std;
typedef unsigned long long int ulli;
typedef long long int lli;

vector<int> get_data()
{
    vector<int> s1;
    int r1;
    cin >> r1;
    int i,j,x;
    repI(i,1,4)
    {
        repI(j,1,4)
        {
            cin >> x;
            if(i==r1) s1.push_back(x);
        }
    }
    return s1;
}

main()
{
    int T;
    cin >> T;
    int tot = T;
    while(T--)
    {
        vector<int> s1;
        vector<int> s2;
        vector<int> s3;
        s1 = get_data();
        s2 = get_data();
        sort(s1.begin(),s1.end());
        sort(s2.begin(),s2.end());
        set_intersection(s1.begin(),s1.end(),s2.begin(),s2.end(),back_inserter(s3));
        //cout << s3.size() << endl;
        int sz = s3.size();
        if (sz==1) cout << "Case #" << tot-T << ": " << s3[0] << endl;
        else if (sz>1) cout << "Case #" << tot-T << ": Bad magician!" << endl;
        else if (sz==0) cout << "Case #" << tot-T << ": Volunteer cheated!" << endl;
    }
}

