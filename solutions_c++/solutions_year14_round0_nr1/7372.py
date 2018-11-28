#include<iostream>
#include<algorithm>
#include<iterator>
#include<set>
using namespace std;
#define N 4
#define BAD "Bad magician!"
#define CHEAT "Volunteer cheated!"
int main(){
    int n,temp;
    cin>>n;
    for(int t=0;t<n;t++){
        int k;
        set<int> a,b;
        cin>>k;
        for(int i=0;i<N;i++)
            for(int j=0;j<N;j++){
                cin>>temp;
                if(i==k-1) a.insert(temp);
            }
        cin>>k;
        for(int i=0;i<N;i++)
            for(int j=0;j<N;j++){
                cin>>temp;
                if(i==k-1) b.insert(temp);
            }
        //Magic
        set<int> c;
        set_intersection(a.begin(),a.end(),b.begin(),b.end(),inserter(c,c.begin()));
        cout<<"Case #"<<t+1<<": ";
        if(c.size()==1)     cout<<*c.begin();
        else if(c.size()>1) cout<<BAD;
        else                cout<<CHEAT;
        cout<<endl;
        a.clear(); b.clear(); c.clear();
    }
}
