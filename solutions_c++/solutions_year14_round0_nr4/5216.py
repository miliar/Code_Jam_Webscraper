#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    vector < double > tab;
    vector < double > tab2;
    vector < double > wtab;
    vector < double > wtab2;

  //  tab.push_back( 0 );
    int war,dwar,w,w2,i,j,T,N;
    bool end;
    double x;
    cin>>T;
    for(i=1;i<=T;i++)
	{
	end=0;
	w=0;w2=0,war=0;dwar=0;
	tab.clear();tab2.clear();wtab.clear();wtab2.clear();
	cout<<"Case #"<<i<<": ";
	cin>>N;
	for(j=0;j<N;j++) {cin>>x;tab.push_back(x);wtab.push_back(x);}
	for(j=0;j<N;j++) {cin>>x;tab2.push_back(x);wtab2.push_back(x);}

	sort( tab.begin(), tab.end() );
        sort( tab2.begin(), tab2.end() );
	sort( wtab.begin(), wtab.end() );
        sort( wtab2.begin(), wtab2.end() );
// poczatek dwar
	while (!end) {
		w2=0;
		while (w2<wtab2.size() && wtab[w2]>wtab2[w2]) w2++;
		if (w2<wtab2.size()) {
			wtab.erase(wtab.begin());wtab2.pop_back();}	
		else end=1;
		}
		cout<<wtab.size();

//poczatek war
	w=0;w2=0;end=0;
	while (!end) {
		w2=0;
		while (w2<tab2.size() && tab[w]>tab2[w2]) w2++;
		if (w2<tab2.size()) {
			tab.erase(tab.begin());tab2.erase(tab2.begin()+w2);}	
		else end=1;
		}
	cout<<" "<<tab.size()<<endl;
	}
    return 0;
}
