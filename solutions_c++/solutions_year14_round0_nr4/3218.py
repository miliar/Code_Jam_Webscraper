#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>


using namespace std;


int PlayOptimalKen(vector<double>& ken, double naomi_val)
{
  int min_index = -1;
  for(int j=0; j<ken.size(); j++)
    if (ken[j]!=0 && ken[j]>naomi_val)
    {
      // choose min among items > naomi_val
      if (min_index == -1) min_index=j;
      else if (ken[j]<ken[min_index]) min_index=j;
    }

  if (min_index==-1)
  {
    // no piece is > naomi_val, return the min then
    for(int i=0; i<ken.size(); i++)
      if (ken[i]!=0)
      {
        if (min_index == -1) min_index=i;
        else if (ken[i]<ken[min_index]) min_index=i;
      }
  }

  return min_index;
}

int SolveWar(vector<double>& naomi, vector<double>& ken)
{
  int points = 0;
  int n = naomi.size();
  std::sort(naomi.begin(), naomi.end());
  for(int i=0; i<n; i++)
  {
    int ken_index = PlayOptimalKen(ken, naomi[i]);
    if (naomi[i] > ken[ken_index]) points++;
    ken[ken_index]=0;
  }
  return points;
}

int SolveDeceitWar(vector<double>& naomi, vector<double>& ken)
{
  int points = 0;
  int n = naomi.size();

  std::sort(naomi.begin(), naomi.end());
  std::sort(ken.begin(), ken.end());
  
  // alternate approach:
  int i_n = 0;
  int i_k = 0;
  while(naomi[i_n]<ken[i_k]) i_n++;
  while(i_n<n)
  {
    if (naomi[i_n]>ken[i_k])
    {
      points++;
      i_n++;
      i_k++;
    }
    else
    {
      i_n++;
    }
  }

  return points;
}
int main()
{
  ifstream in_f("D-large.in");
  ofstream out_f("D-large.out");
  
  int test_cases = 0;
  in_f >> test_cases;

  for(int tc=0; tc<test_cases; tc++)
  {
    // READ
    int n;
    in_f >> n;
    vector<double> naomi(n);
    vector<double> ken(n);
    for(int i=0; i<n; i++) in_f >> naomi[i];
    for(int i=0; i<n; i++) in_f >> ken[i];
  
    // SOLVE
    vector<double> naomi_bak=naomi;
    vector<double> ken_bak=ken;
    vector<double> naomi2=naomi;
    vector<double> ken2=ken;

    int dw = SolveDeceitWar(naomi, ken);
    int w = SolveWar(naomi2, ken2);

    out_f << "Case #" << tc+1 << ": ";
    out_f << dw << " " << w; 
    out_f << endl;
  }

  in_f.close();
  out_f.close();
}
