#include<iostream>
#include<vector>
#include<set>
using namespace std;
int main(){
    int T;
    freopen("D:\\a.txt","r",stdin);
    freopen("D:\\out.txt","w",stdout);
    cin>>T;
    for (int t=1;t<=T;t++){
        int a[10][10];
        int r1,r2;
        cin>>r1;
        for (int i=0;i<4;i++)
            for (int j=0;j<4;j++)
                cin>>a[i][j];
        r1--;
        set<int> s;
        for (int i=0;i<4;i++) s.insert(a[r1][i]);
        cin>>r2;
        for (int i=0;i<4;i++)
            for (int j=0;j<4;j++)
                cin>>a[i][j];
        r2--;
        vector<int> ans;
        for (int i=0;i<4;i++) if (s.find(a[r2][i])!=s.end()){
            ans.push_back(a[r2][i]);
        }
        cout<<"Case #"<<t<<": ";
        if (ans.size()==0) cout<<"Volunteer cheated!"<<endl;
        else if (ans.size()>1) cout<<"Bad magician!"<<endl;
        else cout<<ans[0]<<endl;
    }

}
