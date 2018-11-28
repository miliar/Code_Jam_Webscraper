#include<iostream>
#include<algorithm>
using namespace std;

int d[1000];

int eat(int count)
{
  /* for(int i=0;i<count;i++)
    cout<<d[i]<<" ";
    cout<<endl;*/
    
  bool zeroed=true;
  for(int i=0;i<count;i++)
    if(d[i]>0)
      zeroed=false;

  if(zeroed)
    return 0;
  
  int sec1;
  int sec2;
 
  for(int i=0;i<count;i++)
    d[i]--;

  sec2 = 1 + eat(count);

  for(int i=0;i<count;i++)
    d[i]++;

  int maxi=0;
  for(int i=0;i<count;i++)
    if(d[i]>d[maxi])
      maxi=i;

  int rt;
  for(rt=1;rt*rt<=d[maxi];rt++);
  
  d[count]= (rt-1)*(rt-1)== d[maxi]? rt-1: rt;
  if(d[count] > 1 && (d[maxi]-d[count]) > 1)
    {
      d[maxi] -= d[count];
      sec1 = 1 + eat(count + 1);
      
      d[maxi] += d[count];
    }
  else
    sec1 = sec2;

   d[count]=d[maxi]/2;
   if(d[count] > 1 && (d[maxi] - d[count]) > 1)
    {
      d[maxi] -= d[count];
      sec1 = std::min(sec1, 1 + eat(count + 1));
      d[maxi] += d[count];
    }
   else
     sec1=sec2;
  
  return std::min(sec1, sec2);
}

int main()
{
  int dc, sec, ndc, zeroed;;
  int t;
  cin>>t;
  for(int cases=1;cases<=t;cases++)
    {
      cin>>dc;
      for(int i=0;i<dc;i++)
	{
	  cin>>d[i];
	}

      int sec = eat(dc);
      cout<<"Case #"<<cases<<": "<<sec<<endl;
    }
}
