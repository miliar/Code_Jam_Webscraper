#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

int a,b;

int gr2[10][10];
int gr1[10][10];

int main() {
	freopen("inp.txt","rt",stdin);
    freopen("out.txt","wt",stdout);
    int gt;
	cin>>gt;
    for(int run=1;run<=gt;run++)
	{
	    cin>>a;
	    for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin>>gr1[i][j];

        cin>>b;
	    for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin>>gr2[i][j];

        vector<int> res;
        a--;b--;

        for(int j=0;j<4;j++){
            for(int k=0;k<4;k++) if(gr1[a][j]==gr2[b][k]) res.push_back(gr1[a][j]);
        }
        printf("Case #%d: ",run);
        if(res.size()==0) cout<<"Volunteer cheated!\n";
        else if(res.size()>1) cout<<"Bad magician!\n";
        else cout<<res[0]<<endl;


	}





	return 0;
}

