#include <iostream>
#include <fstream>

using namespace std;
string pp[17];
string rr[17];
string ss[17];
int px[17];int py[17];int pz[17];
int rx[17];int ry[17];int rz[17];
int sx[17];int sy[17];int sz[17];
int main()
{
    freopen("a.in","r",stdin);
    ifstream fp("p1.out");
    ifstream fr("r1.out");
    ifstream fs("s1.out");
    ifstream fp1("p");
    ifstream fr1("r");
    ifstream fs1("s");
    ofstream f2("a.out");
    //s>p p>r r>s
    int t;
    cin >> t;
    for (int i=0;i<=15;i++)
    {
        fp >> pp[i];
        fr >> rr[i];
        fs >> ss[i];
        fp1>> px[i] >> py[i] >> pz[i];
        fr1>> rx[i] >> ry[i] >> rz[i];
        fs1>> sx[i] >> sy[i] >> sz[i];
    }
    for (int ju=1;ju<=t;ju++)
    {
    f2 << "Case #" << ju << ": ";
        int n,p,r,s;
        cin >> n >> r >> p >> s;
        if (n==1)
        {
            if (r==2||p==2||s==2){f2 << "IMPOSSIBLE" << endl;continue;}
            if (r==0){f2 << "PS" << endl;continue;}
            if (p==0){f2 << "RS" << endl;continue;}
            if (s==0){f2 << "PR" << endl;continue;}
        }
        //p - победа
        int imp=23;
        string res="Z";
        int p1,r1,s1;
        if (px[n]==p&&py[n]==r&&pz[n]==s){imp=22;string s6=pp[n];res=s6;}

        if (rx[n]==p&&ry[n]==r&&rz[n]==s){imp=22;string s6=rr[n];if (s6<res){res=s6;}}
        if (sx[n]==p&&sy[n]==r&&sz[n]==s){imp=22;string s6=ss[n];if (s6<res){res=s6;}}

    if (imp==23){f2 << "IMPOSSIBLE" << endl;continue;}

    f2 << res << endl;


    }

    return 0;
}
