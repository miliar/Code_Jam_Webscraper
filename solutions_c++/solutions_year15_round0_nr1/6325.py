#include<fstream>
#include<string>
using namespace std;

int main()
{
 int t;
 int n;
 string s;
 ifstream fin("A-large.in");
 ofstream fout("out.out");
 fin>>t;
 for(int j=0;j<t;j++)
 {
  fin>>n;
  fin>>s;
  int count=0;
  int avai=0;
  for(int i=0;i<=n;i++)
   if(s[i]!='0')
   {
    if(avai<i)
	{
	 avai+=(i-avai);
	}
	count+=s[i]-'0';
    avai+=s[i]-'0';
   }
   
  fout<<"Case #"<<j+1<<": "<<avai-count<<endl;
 }
}

