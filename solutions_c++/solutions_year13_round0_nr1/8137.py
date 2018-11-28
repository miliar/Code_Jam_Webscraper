#include <iostream>
#include <cstdlib>
#include <vector>
#include <fstream>
using namespace std;
void init(vector<vector< int > > &board,
      vector<pair<int,int > > &horizontal,
      vector<pair<int,int > > &vertical,
      vector<pair<int,int > > &diagonal)
      {
          horizontal.resize(4);
          vertical.resize(4);
          
          board.resize(4);
          for(int g=0;g<4;g++)
          {
          horizontal[g].first=0;
          horizontal[g].second=0;
          vertical[g].first=0;
          vertical[g].second=0;          
          board[g].resize(4);
          }
          diagonal.resize(2);
          diagonal[0].first=0;
          diagonal[0].second=0;          
          diagonal[1].first=0;
          diagonal[1].second=0;                    
      }

main()
{
      vector<vector< int > > board;
      vector<pair<int,int > > horizontal;
      vector<pair<int,int > > vertical;
      vector<pair<int,int > > diagonal;
      int runs;
      ifstream in("A-small-attempt0.in");
      in>>runs;
      char T;
      ofstream out("A-small-attempt0.out");
      for(int i=1;i<=runs;i++)
      {
      init(board,horizontal,vertical,diagonal);
       int empty=0;
       for(int g=0;g<4;g++)
       {
        for(int h=0;h<4;h++)
        {
          in>>T;
          if(T=='.')
          {
           board[g][h]=0;
           empty++;
           }
         else if(T=='O')
         board[g][h]=-1;
         else if(T=='X')
         board[g][h]=1;
         else 
         board[g][h]=2;     
        }        
       }        
             /* for(int g=0;g<4;g++)
              {
               for(int h=0;h<4;h++)
               {
                 cout<<board[g][h]<<" ";       
               }        
               cout<<endl;
              }
              cout<<endl;
      */
      bool end= false;
      for(int g=0;g<4;g++)
      {
              int h;
         for(h=0;h<4;h++)
         {
             horizontal[g].first += board[g][h]!=2?board[g][h]:1;
             horizontal[g].second += board[g][h]!=2?board[g][h]:-1;
             vertical[g].first +=board[h][g]!=2?board[h][g]:1;
             vertical[g].second += board[h][g]!=2?board[g][h]:-1;             
         }
         diagonal[0].first+=board[g][g]!=2?board[g][g]:1;
         diagonal[0].second+=board[g][g]!=2?board[g][g]:-1;                  
         diagonal[1].first+=board[g][3-g]!=2?board[g][3-g]:1;
         diagonal[1].second+=board[g][3-g]!=2?board[g][3-g]:-1;                  
         if(abs(horizontal[g].first)==4)
           { 
            out<<"Case #"<<i<<": "<<(horizontal[g].first>0?"X won":"O won");
            out<<endl;                                                   
                        end=true;
            break;
            
            }
         else  if(abs(horizontal[g].second)==4)
           {
                           out<<"Case #"<<i<<": "<<(horizontal[g].second>0?"X won":"O won");
                out<<endl; 
            end=true;                                                                  
            break;                
           }
         else  if(abs(vertical[g].first)==4)
         {
            out<<"Case #"<<i<<": "<<(vertical[g].first>0?"X won":"O won");               
            out<<endl;   
            end=true;                                                            
            break;            
         }
         else  if(abs(vertical[g].second)==4)
         {
            out<<"Case #"<<i<<": "<<(vertical[g].second>0?"X won":"O won");                              
                out<<endl;
            end=true;                
            break;                
         }
         else  if(abs(diagonal[0].first)==4)
         {
            out<<"Case #"<<i<<": "<<(diagonal[0].first>0?"X won":"O won");                                
           
            out<<endl;   
            end=true;            
            break;            
         }
         else  if(abs(diagonal[0].second)==4)
         {
            out<<"Case #"<<i<<": "<<(diagonal[0].second>0?"X won":"O won");  
            out<<endl;   
            end=true;            
            break;            
         }
         else  if(abs(diagonal[1].first)==4)
         {
            out<<"Case #"<<i<<": "<<(diagonal[1].first>0?"X won":"O won");                 
            out<<endl;
            end=true;
            break;            
         }
         else  if(abs(diagonal[1].second)==4)
         {
            out<<"Case #"<<i<<": "<<(diagonal[1].second>0?"X won":"O won");                                
            out<<endl;
            end=true;            
            break;            
         }

      }
      /*cout<<diagonal[0].first<<" "<<diagonal[0].second<<endl;
            cout<<diagonal[1].first<<" "<<diagonal[1].second<<endl;*/
      if(empty>0&&end==false)
      out<<"Case #"<<i<<": "<<"Game has not completed"<<endl;
      else if(end==false)
      out<<"Case #"<<i<<": "<<"Draw"<<endl;
      }
      return 0;
}
