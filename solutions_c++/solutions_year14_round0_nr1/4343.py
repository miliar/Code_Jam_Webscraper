#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;
vector<int> getIntLine()
{
  vector<int> rep;
  for(int i = 0; i < 4; i++)
  {
    int temp;
    scanf("%d", &temp);
    rep.push_back(temp);
  }
  return rep;
}

int main()
{
  int nbtests;
  scanf("%d",&nbtests);
  for(int t = 0; t < nbtests;t++)
  {
    int rep1,rep2;
    vector<int> ligrep1, ligrep2;
    scanf("%d", &rep1);
    for(int ligne = 1; ligne <= 4; ligne ++)
    {
      vector<int> temp = getIntLine();
      if(ligne == rep1)
	ligrep1 = temp;
    }
    scanf("%d",&rep2);
    for(int ligne = 1; ligne <= 4; ligne++)
    {
      vector<int> temp = getIntLine();
      if(ligne == rep2)
	ligrep2 = temp;
    }
    vector<int> reponse(4);
    sort(ligrep1.begin(), ligrep1.end());
    sort(ligrep2.begin(),ligrep2.end());
    vector<int>::iterator it;
    it = set_intersection( ligrep1.begin(), ligrep1.end(), ligrep2.begin(), ligrep2.end(), reponse.begin());
    reponse.resize(it - reponse.begin());
    printf("Case #%d: ", t+1);
    switch(reponse.size())
    {
      case 0 :
	printf("Volunteer cheated!");
	break;
      case 1:
	printf("%d",reponse[0]);
	break;
      default:
	printf("Bad magician!");

    }
    printf("\n");
  }
  return 0;
}
