#include<fstream>
using namespace std;
int main()
{
    fstream input("input.in",ios::in);
    fstream output("output.out",ios::out);
    int t,i,x,r,c;
    input>>t;
    for(i=0;i<t;i++)
    {
        input>>x>>r>>c;
        if((r%x==0&&c>=x-1)||(c%x==0&&r>=x-1))
            output<<"Case #"<<i+1<<": GABRIEL\n";
        else
            output<<"Case #"<<i+1<<": RICHARD\n";
    }
    return 0;
}
