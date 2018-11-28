#include <iostream>
#include <fstream>

using namespace std;

ofstream myfile;

void test(int x, int r, int c, int n)
{
    if(x==1)
        myfile << "Case #" << n <<": GABRIEL\n";
    else
    {
        if( x>r && x>c )
            myfile << "Case #" << n <<": RICHARD\n";
        else
        {
           if(x==2)
           {
               if((r*c)%2==1)
                myfile << "Case #" << n <<": RICHARD\n";
               else
                myfile << "Case #" << n <<": GABRIEL\n";
           }
           else if(x==3)
           {
                if(r*c==6 || r*c==9 || r*c==12 )
                    myfile << "Case #" << n <<": GABRIEL\n";
                else
                    myfile << "Case #" << n <<": RICHARD\n";
           }
           else
           {
                if( r*c<12 )
                    myfile << "Case #" << n <<": RICHARD\n";
                else
                    myfile << "Case #" << n <<": GABRIEL\n";
           }

        }
    }
}

void rea()
{
    ifstream read("C:\\Users\\Melih\\Desktop\\input.txt");
    int lines,x,r,c;
    int s[1005];
    read>>lines;//number of lines
    for(int i=1;i<=lines;i++)
    {
            read>>x>>r>>c;
            test(x,r,c,i);
    }

}

int main () {
    myfile.open ("C:\\Users\\Melih\\Desktop\\output.txt");
    rea();
    myfile.close();
    return 0;
}
