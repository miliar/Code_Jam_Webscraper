#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main () {
  string line;
  string twode[4][4];
  int i=0,j=0,t,o,x,flag=0,emp=0,casec=1;
  ifstream myfile ("input.in");
  ofstream outp ("output.out");
  if (myfile.is_open())
  {
      getline (myfile,line);     
      while ( myfile.good() )
    {
        getline (myfile,line);
        for(j=0;j<4&&i<4;++j)
          {
                twode[i][j]=line[j];
                //cout<<twode[i][j];
                //cout<<i<<j;
          }
        ++i;
        if(i>=4)
        {            
            outp<<"Case #"<<casec<<": ";
            ++casec;
            //Row check
            for(i=0;i<4&&flag==0;++i)
            {
            o=0;
            x=0;
            t=0;
                for(j=0;j<4;++j)
            {
                if(twode[i][j]=="O")
                    ++o;
                if(twode[i][j]=="X")
                    ++x;
                if(twode[i][j]=="T")
                    ++t;
            }
                if(o==4 || (o==3&&t>=1))
                {
                    outp<<"O won"<<endl; 
                    flag=1;
                }
                    
                if(x==4 || (x==3&&t>=1))
                {
                    outp<<"X won"<<endl;
                    flag=1;
                }
                    
            }
            //Column check
            for(i=0;i<4&&flag==0;++i)
            {
            o=0;
            x=0;
            t=0;
                for(j=0;j<4;++j)
            {
                if(twode[j][i]=="O")
                    ++o;
                if(twode[j][i]=="X")
                    ++x;
                if(twode[j][i]=="T")
                    ++t;
            }
                if(o==4 || (o==3&&t>=1))
                {
                    outp<<"O won"<<endl; 
                    flag=1;
                }
                    
                if(x==4 || (x==3&&t>=1))
                {
                    outp<<"X won"<<endl;
                    flag=1;
                }
            }
            //Diagonal check 1
            //if((twode[0][0]==twode[1][1]&&twode[1][1]==twode[2][2]&&twode[2][2]==twode[3][3]) && (twode[0][0]!="."))
                    //cout<<twode[0][0]<<" won";
            o=0;
            x=0;
            t=0;
                for(i=0;i<4&&flag==0;++i)
            {
                if(twode[i][i]=="O")
                    ++o;
                if(twode[i][i]=="X")
                    ++x;
                if(twode[i][i]=="T")
                    ++t;
            }
                if(o==4 || (o==3&&t>=1))
                {
                    outp<<"O won"<<endl; 
                    flag=1;
                }
                    
                if(x==4 || (x==3&&t>=1))
                {
                    outp<<"X won"<<endl;
                    flag=1;
                }
            
           //Diagonal check 2
            
            o=0;
            x=0;
            t=0;
            j=3;
                for(i=0;i<4&&flag==0;++i)
            {
                if(twode[i][j]=="O")
                    ++o;
                if(twode[i][j]=="X")
                    ++x;
                if(twode[i][j]=="T")
                    ++t;
                --j;
            }
                if(o==4 || (o==3&&t>=1))
                {
                    outp<<"O won"<<endl; 
                    flag=1;
                }
                    
                if(x==4 || (x==3&&t>=1))
                {
                    outp<<"X won"<<endl;
                    flag=1;
                }
            
            //Game in progress
            
            for(i=0;i<4&&flag==0;++i)          
              for(j=0;j<4;++j)           
                if(twode[i][j]==".")
                {
                    flag=1;
                    outp<<"Game has not completed"<<endl;
                    break;
                }
            if(flag==0)
            outp<<"Draw"<<endl;            
            i=0;
            getline (myfile,line);
            flag=0;
        }
        //outp << endl;
    }
    myfile.close();
  }

  else cout << "Unable to open file";   
  return 0;
}