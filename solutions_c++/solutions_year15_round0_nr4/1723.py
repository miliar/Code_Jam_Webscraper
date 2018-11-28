#include <iostream>
#include <string>
#include <vector>

using namespace std;

int getAns(int x, int r, int c)
{
    if (r>c) swap(r,c);

    if (x==1) return true;
    if (x==2) return (r*c)%2==0;
    if (x==3)
    {
        if (r==1) return false;
        return (r*c)%3==0;
    }


    //x=4;
    if (c<4) return false;
    return r==3 || r==4;
}

int main()
{
    freopen("D-small-attempt1.in","r",stdin);
    freopen("d.out","w",stdout);

    vector<string> name = {"RICHARD", "GABRIEL"};
    int T;
    cin>>T;
    for (int cas=1; cas<=T; cas++)
    {
        int x,r,c;
        cin>>x>>r>>c;
        int ans = getAns(x,r,c);
        cout<<"Case #"<<cas<<": "<<name[ans]<<endl;
    }

    return 0;
}
