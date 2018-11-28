#include<fstream>
#include<iostream>

using namespace std;


void flip(string &s, int left, int right)
{  //left=0; right=end;
   char temp;
   while(left<right)
   { temp=s[left];
     if(s[right]=='+') s[left]='-'; else s[left]='+';
     if(temp=='+') s[right]='-'; else s[right]='+';
     left++; right--;
   }
   
   if(left==right) 
    { if(s[right]=='+') s[left]='-'; else s[left]='+';
    }
}

int solver(string s)
{ int i,end,left,right,sum=0;
  end=s.size()-1;
  
  for(;;)
  {
  
  while(end>=0 && s[end]=='+') end--;
  
  if(end==-1) return sum;
  if(end==0)  return sum+1;
  
  //if(s[0]=='+') { s[0]='-'; sum++;}
   if(s[0]=='+'){
   
   i=0;
   while(s[i]=='+') i++;
   
   flip(s,0,i-1);
   sum++;
}

  /*left=0; right=end;
  while(left<right)
   { temp=s[left];
     if(s[right]=='+') s[left]='-'; else s[left]='+';
     if(temp=='+') s[right]='-'; else s[right]='+';
     left++; right--;
   }
   
   if(left==right) 
    { if(s[right]=='+') s[left]='-'; else s[left]='+';
    }*/
    
   flip(s,0,end);
   sum++;
}
   return sum;
}


int main()
{ int i,j,n,res;
  string s;
 
  ofstream output;
  output.open("output3.txt");
  
  ifstream input;
  input.open("B-large.in");
  input>>n;
 // cout<<n<<endl;
  for(j=1;j<=n;j++)
  { input>>s; //cout<<s<<endl;
    res=solver(s);
    output<<"Case #"<<j<<": "<<res<<endl; 
    //cout<<j<<" "<<s<<" "<<res<<endl;
   // cout<<j<<endl;
  }
  
 input.close();
 output.close();
   return 0;
}
