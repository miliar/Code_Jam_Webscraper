#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

int main()
{
  
  int t;
  ifstream inFile("pa.txt"); 
  string s;
  
  int xwin=0;
  int owin=0;
  int ncom=0;
  
  ofstream myfile;
  myfile.open ("paout.txt");
  
  if (inFile.is_open())
  {
  
  getline(inFile,s);
 // cout<<"Number of test cases="<<s<<endl;
  
  istringstream buffer(s);
  buffer >> t; 
//  cout<<"my t="<<t<<endl;

  
  //for T
  
  for(int it=1;it<=t;++it)
  {
  
  xwin=0;
  owin=0;
  ncom=0;
  
  
  
  vector <string> v;
  
  
  for(int i=0;i<4;++i)
  {
     inFile>>s;
  //   cout<<s<<endl; 
     //myfile<<s<<endl;
     v.push_back(s);              
  }
  
  // work with v... 
  
  /*
  for(int i=0;i<4;++i)
  {
  	cout<<"           "<<v[i]<<endl;
  }
  */
  
  int nx=0;
  int no=0;
  int tt=0;
  
  for(int i=0;i<4;++i)
  {
   nx=0;
   no=0;
   tt=0;
   
  // cout<<"Testing"<<v[i]<<endl;
   
    for(int j=0;j<4;++j)
    {
       if(v[i][j]=='X')
         ++nx;
       else if(v[i][j]=='O')
          ++no;
        else if(v[i][j]=='T')
          ++tt;
        else if(v[i][j]=='.')
          ncom=1;
                               
    }    
    
  //  cout<<"x="<<nx<<" ny="<<no<<" tt="<<tt<<endl;
    
    if(nx==4 || (nx==3 && tt==1))
      xwin=1;
    else if(no==4 || (no==3 && tt==1))
      owin=1;                        
  }
  
 // cout<<"Testing reverse           asdfasdfasd"<<endl;
  
  for(int i=0;i<4;++i)
  {
   nx=0;
   no=0;
   tt=0;
   
    for(int j=0;j<4;++j)
    {
       if(v[j][i]=='X')
         ++nx;
       else if(v[j][i]=='O')
          ++no;
        else if(v[j][i]=='T')
          ++tt;
        else if(v[j][i]=='.')
          ncom=1;                         
    }    
  //  cout<<"x="<<nx<<" ny="<<no<<" tt="<<tt<<endl;
   
    if(nx==4 || (nx==3 && tt==1))
       xwin=1;
    else if(no==4 || (no==3 && tt==1))
       owin=1;                       
  }
  
  
//  cout<<"DIAGONALLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL"<<endl;
  
   nx=0;
   no=0;
   tt=0;
  for(int i=0;i<4;++i)
  { 
    int j=i;
  //   cout<<"Testing================="<<v[i][j]<<endl;
       if(v[i][j]=='X')
         ++nx;
       else if(v[i][j]=='O')
          ++no;
        else if(v[i][j]=='T')
          ++tt;            
	    
    
  //  cout<<"x="<<nx<<" ny="<<no<<" tt="<<tt<<endl;
    
    if(nx==4 || (nx==3 && tt==1))
          xwin=1;
    else if(no==4 || (no==3 && tt==1))
      owin=1;                        
  }
  
 // cout<<"Testing diagonal"<<endl;
   nx=0;
   no=0;
   tt=0;
  
  for(int i=0;i<4;++i)
  { 
    for(int j=0;j<1;++j)
    {
   //     cout<<"Testing"<<v[i][3-i]<<endl;     
       if(v[i][3-i]=='X')
         ++nx;
       else if(v[i][3-i]=='O')
          ++no;
        else if(v[i][3-i]=='T')
          ++tt;  
	                        
    }    
    
 //   cout<<"x="<<nx<<" ny="<<no<<" tt="<<tt<<endl;
    
     if(nx==4 || (nx==3 && tt==1))
         xwin=1;
	 else if(no==4 || (no==3 && tt==1))
       owin=1;                        
   }
  
  
  /*
  
       if(xwin==1 && owin==0)
         cout<<"XXXXXXXXXXXXXXXXXXX"<<endl;
       else if(xwin==0 && owin==1)
         cout<<"YYYYYYYYYYY"<<endl;
       else if(xwin==0 && owin==0 && ncom==0)
         cout<<"DRAWWWWWWWWWWWWWWWWWW"<<endl;
       else 
	      cout<<"Game has not completed"<<endl;  
  
  */
  
 //Write this to a file
   
  
  // myfile<<"xwin="<<xwin<<" owin="<<owin<<" ncom="<<ncom<<endl;
   
   
 /*  
   cout<<"Case #"<<it<<": ";
 
       if(xwin==1 && owin==0)
         cout<<"X won"<<endl;
       else if(xwin==0 && owin==1)
         cout<<"O won"<<endl;
       else if(xwin==0 && owin==0 && ncom==0)
         cout<<"Draw"<<endl;
       else 
	      cout<<"Game has not completed"<<endl;
 
  */
  
  
  myfile << "Case #"<<it<<": ";
  
       if(xwin==1 && owin==0)
         myfile<<"X won"<<endl;
       else if(xwin==0 && owin==1)
         myfile<<"O won"<<endl;
       else if(xwin==0 && owin==0 && ncom==0)
         myfile<<"Draw"<<endl;
       else 
	      myfile<<"Game has not completed"<<endl;
 
 
   /*
       if(xwin==1 && owin==0)
         cout<<"XXXXXXXXXXXXXXXXXXX"<<endl;
       else if(xwin==0 && owin==1)
         cout<<"YYYYYYYYYYY"<<endl;
       else if(xwin==0 && owin==0 && ncom==0)
         cout<<"DRAWWWWWWWWWWWWWWWWWW"<<endl;
       else 
	      cout<<"Game has not completed"<<endl;  
  */
  
  // T ends here..   
 
   
}
 
 }
 else
   cout<<"Problem Opening file... "<<endl; 
 
  inFile.close();  
  myfile.close();  
    
  /*  
  ofstream myfile;
  myfile.open ("paout.txt");
  myfile << "Writing this to a file.\n";
  myfile.close();
  return 0;    
  */
  
  
  return 1;
}

