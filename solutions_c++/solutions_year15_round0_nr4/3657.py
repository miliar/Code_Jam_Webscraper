/*Author: Anonymous
Insti: Anonymous
Roll: Anonymous*/
#include<fstream>
using namespace std;
/*Author: Anonymous
Insti: Anonymous
Roll: Anonymous*/
int main()
{
    /*Author: Anonymous
Insti: Anonymous
Roll: Anonymous*/
    fstream in("in.in",ios::in);
    fstream out("out.out",ios::out);
    int t,i,x,r,c;
    in>>t;
    /*Author: Anonymous
Insti: Anonymous
Roll: Anonymous*/
    for(i=0;i<t;i++)
    {
        /*Author: Anonymous
Insti: Anonymous
Roll: Anonymous*/
        in>>x>>r>>c;
        if(x>=7)
            out<<"Case #"<<i+1<<": RICHARD\n";
        else if((r%x==0&&c>=x-1)||(c%x==0&&r>=x-1))
            out<<"Case #"<<i+1<<": GABRIEL\n";
        else
            out<<"Case #"<<i+1<<": RICHARD\n";
            /*Author: Anonymous
Insti: Anonymous
Roll: Anonymous*/
    }
    /*Author: Anonymous
Insti: Anonymous
Roll: Anonymous*/
    return 0;
}
/*Author: Anonymous
Insti: Anonymous
Roll: Anonymous*/
