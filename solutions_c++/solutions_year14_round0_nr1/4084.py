#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;


int main()
{
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-small-attempt1.out", "w", stdout);

    int t;
    cin>>t;
    for(int i=0; i<t; i++){

        int ans1, ans2, temp;
        vector <int> cards1(4), cards2(4);

        cin>>ans1;
        for(int r=0; r<4; r++){
            for(int c=0; c<4; c++){
                if(r==(ans1-1))
                    cin>>cards1[c];
                else
                    cin>>temp;
            }
        }

        cin>>ans2;
        for(int r=0; r<4; r++){
            for(int c=0; c<4; c++){
                if(r==ans2-1)
                    cin>>cards2[c];
                else
                    cin>>temp;
            }
        }

    sort(cards1.begin(), cards1.end());
    sort(cards2.begin(), cards2.end());

    vector<int> v;
    set_intersection(cards1.begin(), cards1.end(), cards2.begin(), cards2.end(), back_inserter(v));

    cout<<"Case #"<<i+1<<": ";
    if(v.size()==0) cout<<"Volunteer cheated!";
    else if (v.size()>1) cout<<"Bad magician!";
    else cout<<v[0];
    cout<<endl;
    v.clear();
    }

    return 0;
}
