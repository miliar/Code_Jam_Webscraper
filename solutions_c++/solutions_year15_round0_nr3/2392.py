#include <iostream>
#include <string>
#include <vector>

using namespace std;

int quaternion_multiply(int term1, int term2)
{
     switch(term1)
     {
     case 1: switch(term2)
          {
          case 1: return 1;
          case -1: return -1;
          case 'i': return 'i';
          case -1*'i': return -1*'i';
          case 'j': return 'j';
          case -1*'j': return -1*'j';
          case 'k': return 'k';
          case -1*'k': return -1*'k';
          }
     case -1: switch(term2)
          {
          case -1: return 1;
          case 1: return -1;
          case -1*'i': return 'i';
          case 'i': return -1*'i';
          case -1*'j': return 'j';
          case 'j': return -1*'j';
          case -1*'k': return 'k';
          case 'k': return -1*'k';
          }
     case 'i': switch(term2)
          {
          case 1: return 'i';
          case -1: return -1*'i';
          case 'i': return -1;
          case -1*'i': return 1;
          case 'j': return 'k';
          case -1*'j': return -1*'k';
          case 'k': return -1*'j';
          case -1*'k': return 'j';
          }
     case -1*'i': switch(term2)
          {
          case -1: return 'i';
          case 1: return -1*'i';
          case -1*'i': return -1;
          case 'i': return 1;
          case -1*'j': return 'k';
          case 'j': return -1*'k';
          case -1*'k': return -1*'j';
          case 'k': return 'j';
          }
     case 'j': switch(term2)
          {
          case 1: return 'j';
          case -1: return -1*'j';
          case 'i': return -1*'k';
          case -1*'i': return 'k';
          case 'j': return -1;
          case -1*'j': return 1;
          case 'k': return 'i';
          case -1*'k': return -1*'i';
          }
     case -1*'j': switch(term2)
          {
          case -1: return 'j';
          case 1: return -1*'j';
          case -1*'i': return -1*'k';
          case 'i': return 'k';
          case -1*'j': return -1;
          case 'j': return 1;
          case -1*'k': return 'i';
          case 'k': return -1*'i';
          }
     case 'k': switch(term2)
          {
          case 1: return 'k';
          case -1: return -1*'k';
          case 'i': return 'j';
          case -1*'i': return -1*'j';
          case 'j': return -1*'i';
          case -1*'j': return 'i';
          case 'k': return -1;
          case -1*'k': return 1;
          }
     case -1*'k': switch(term2)
          {
          case -1: return 'k';
          case 1: return -1*'k';
          case -1*'i': return 'j';
          case 'i': return -1*'j';
          case -1*'j': return -1*'i';
          case 'j': return 'i';
          case -1*'k': return -1;
          case 'k': return 1;
          }
     }
}

int main()
{
     int cases;
     cin >> cases;
     for(int z=0; z<cases; z++)
     {
          //Input
          int L, X;
          cin >> L >> X;
          string dumbass;
          cin >> dumbass;
          string fullass = "";
          for(int j=0; j<X; j++)
               fullass+=dumbass;

          //Algorithm
          vector<int> ipositions, kpositions;

          //Possible i end positions
          int mustbei = 1;
          for(int i=0; i<fullass.length()-2; i++)
          {
               mustbei = quaternion_multiply(mustbei,fullass[i]);
               if(mustbei=='i')
                    ipositions.push_back(i);
          }

          //Possible k start positions
          int mustbek = 1;
          for(int k = fullass.length() - 1; k>=2; k--)
          {
               mustbek = quaternion_multiply(fullass[k],mustbek);
               if(mustbek=='k')
                    kpositions.push_back(k);
          }

          //Accumulate entirety of j
          vector<int> jsequence;
          jsequence.reserve(fullass.length());
          int current_j = 1;
          for(int j=0; j<fullass.length(); j++)
          {
               current_j = quaternion_multiply(current_j,fullass[j]);
               jsequence.push_back(current_j);
          }
          
          bool yes = false;
          for(int i=0; !yes && i<ipositions.size(); i++)
               for(int k=kpositions.size()-1; !yes && k>=0; k--)
               {
                    if(ipositions[i]+1 > kpositions[k]-1)
                         continue;
                    
                    int seqstart = ipositions[i]+1;
                    int seqend = kpositions[k]-1;
                    int multiplier = jsequence[seqend];

                    if(seqstart==seqend)
                         yes = fullass[seqstart]=='j';
                    else if(seqend-seqstart==1)
                         yes = quaternion_multiply(fullass[seqstart],fullass[seqend]) == 'j';
                    else if(jsequence[seqstart]==-1)
                    {
                         multiplier = -multiplier;
                         yes = quaternion_multiply(fullass[seqstart],multiplier) == 'j';
                    }
                    else if(jsequence[seqstart]!=1)
                    {
                         multiplier = quaternion_multiply(-jsequence[seqstart],multiplier);
                         yes = quaternion_multiply(fullass[seqstart],multiplier) == 'j';
                    }
                    else //jsequence[seqstart]==1
                         yes = quaternion_multiply(fullass[seqstart],multiplier) == 'j';
               }

          cout << "Case #" << (z+1) << ": " << (yes ? "YES" : "NO") << endl;
     }

     return 0;
}
