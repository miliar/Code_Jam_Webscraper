//{ ---------- C headers
# include <cstdio>
# include <cstring>
# include <cmath>
# include <cstdlib>
# include <cctype>
//}

//{ ---------- C++ headers
# include <iostream>
# include <string>
# include <algorithm>
# include <vector>
# include <queue>
# include <stack>
# include <map>
# include <sstream>
//}
using namespace std;

//{ ---------- Movements
/*int dx[]={1,-1,0,0}, dy[]={0,0,1,-1};*/ // 4 way movement
/*int dx[]={1,0,-1,0,1,-1,1,-1}, dy[]={0,1,0,-1,1,1,-1,-1};*/ // 8 way movement
//}

int main()
{
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);

    int CASE,cse=1;

    cin>>CASE;
    while(CASE--)
    {
        int ans;

        //first one
        cin>>ans; ans--;
        vector <int> first;
        for(int i=0; i<4; i++) for(int j=0; j<4; j++)
        {
            int card; cin>>card;
            if(i==ans) first.push_back(card);
        }

        //second one
        cin>>ans; ans--;
        vector <int> second;
        for(int i=0; i<4; i++) for(int j=0; j<4; j++)
        {
            int card; cin>>card;
            if(i==ans) second.push_back(card);
        }

        //matching
        int MATCH=0, MATCH_CARD;
        for(int i=0; i<4; i++) for(int j=0; j<4; j++)
        {
            if(first[i]==second[j])
            {
                MATCH++;
                MATCH_CARD=first[i];
            }
        }

        //result
        printf("Case #%d: ",cse++);
        if(MATCH==1) cout<<MATCH_CARD<<endl;
        else if(MATCH>1) cout<<"Bad magician!"<<endl;
        else cout<<"Volunteer cheated!"<<endl;
    }

    return 0;
}
