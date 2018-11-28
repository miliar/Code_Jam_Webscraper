#include <vector>
#include <list>
#include <map>
#include <fstream>
#include <iostream>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>


using namespace std;


ifstream fin("A-small-attempt0.in");
ofstream fout("A-out.out");
int main(){
int t;
fin>>t;
for (int tests=0;tests<t;tests++){
int sel1,sel2;
vector<int> rows1[4],rows2[4];
vector<int> intersected(20);
fin>>sel1;
for (int i=0;i<4;i++)
for (int j=0;j<4;j++){
    int temp;
    fin>>temp;
    rows1[i].push_back(temp);
}
fin>>sel2;
for (int i=0;i<4;i++)
for (int j=0;j<4;j++){
    int temp;
    fin>>temp;
    rows2[i].push_back(temp);
}
    
sort(rows1[sel1-1].begin(),rows1[sel1-1].end());
sort(rows2[sel2-1].begin(),rows2[sel2-1].end());
std::vector<int>::iterator it;
it=set_intersection (rows1[sel1-1].begin(), rows1[sel1-1].end(), rows2[sel2-1].begin(), rows2[sel2-1].end(), intersected.begin());
intersected.resize(it-intersected.begin());
 
for (int j=0;j<4;j++)
    cout<<rows1[sel1-1][j]<<" ";
    cout<<endl;
for (int j=0;j<4;j++)
    cout<<rows2[sel2-1][j]<<" ";
    cout<<endl;
fout<<"Case #"<<tests+1<<": ";
if (intersected.size()==0)fout<<"Volunteer cheated!"<<endl;
if (intersected.size()==1)fout<<intersected[0]<<endl;
if (intersected.size()>1)fout<<"Bad magician!"<<endl;
//for (int i=0;i<intersected.size();i++)fout<<intersected[i]<<" ";
//fout<<endl;


}


cout<<endl;
//system("pause");
return 0;
}
