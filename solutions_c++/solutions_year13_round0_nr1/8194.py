#include<iostream>
#include<vector>
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)
using namespace std ;
int main()
{
READ("A-small-attempt0.in");
WRITE("A-small-attempt0.out");
    int N ;
    cin>>N ;
    for(int t =0 ; t<N ; t++){
    vector<string> arr ;
    for(int i =0 ; i<4 ; i++)
    {
                    string c ;
                    cin>>c ;
                    arr.push_back(c) ;
    }
    bool b = false ;
    for(int i =0 ; i<4 ; i++)
    {
            for(int j = 0 ; j<4 ; j++)
            {
                   if ((arr[i].find("OOO") != string::npos && arr[i].find("T")!=string::npos)||arr[i].find("OOOO") != string::npos)
                   {
                              cout<<"Case #"<<t+1<<": "<<"O won"<<endl;
                              b = true ;
                              break ; 
                   }
                   else if ((arr[i].find("XXX") != string::npos && arr[i].find("T")!=string::npos)||arr[i].find("XXXX") != string::npos)
                   {
                        cout<<"Case #"<<t+1<<": "<<"X won"<<endl ;
                        b=true ;
                        break ;
                   }
            }
            if (b)break ;
    }
    if (!b)
    {
for(int j = 0 ; j<4 ; j++)
    {
            string s = "" ;
             for(int i =0 ; i<4 ; i++)
            {
                  s+=arr[i][j] ;
            }
            if ((s.find("OOO") != string::npos && s.find("T")!=string::npos)||s.find("OOOO") != string::npos )
                   {
                              cout<<"Case #"<<t+1<<": "<<"O won"<<endl; 
                              b=true ;
                              break; 
                   }
                   else if ((s.find("XXX") != string::npos && s.find("T")!=string::npos)||s.find("XXXX") != string::npos)
                   {
                        cout<<"Case #"<<t+1<<": "<<"X won"<<endl ;
                        b=true ;
                        break ;
                   }
                   if (b)break ;
    }
}
 string s = "" ;
if (!b){
   s="" ;
    for(int i =0 ; i<4 ; i++)
    {
            for(int j = 0 ; j<4 ; j++)
            {
                  if (i==j)s+=arr[i][j] ;
            }
             if ((s.find("OOO") != string::npos && s.find("T")!=string::npos)||s.find("OOOO") != string::npos )
                   {
                              cout<<"Case #"<<t+1<<": "<<"O won"<<endl; 
                              b=true ;
                              break ;
                   }
                   else if ((s.find("XXX") != string::npos && s.find("T")!=string::npos)||s.find("XXXX") != string::npos)
                   {
                        cout<<"Case #"<<t+1<<": "<<"X won"<<endl ;
                        b=true ;
                        break ;
                   }
    }
}
if (!b){
    s = "" ;
    s+=arr[0][3] ;
    s+=arr[1][2] ;
    s+=arr[2][1] ;
    s+=arr[3][0] ;
     if ((s.find("OOO") != string::npos && s.find("T")!=string::npos)||s.find("OOOO") != string::npos )
                   {
                              cout<<"Case #"<<t+1<<": "<<"O won"<<endl;
                             b=true ;
                   }
                   else if ((s.find("XXX") != string::npos && s.find("T")!=string::npos)||s.find("XXXX") != string::npos)
                   {
                        cout<<"Case #"<<t+1<<": "<<"X won"<<endl ;
                       b=true ;
                   }
                   }
                   if (!b)
                   {
                     for(int i = 0 ; i< arr.size() ; i++)
                     {
                             if (arr[i].find(".")!=string::npos)
                             {
                                                                cout<<"Case #"<<t+1<<": "<<"Game has not completed"<<endl ;
                                                                b=true ;
                                                                break ;
                                                                
                             }
                     }
                     if (!b)cout<<"Case #"<<t+1<<": "<<"Draw"<<endl ;     
                   }         
                   }
                   
    //system("pause");
    
}
