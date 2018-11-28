#include<fstream>
#include<string>
#include<vector>
using namespace std;

struct G
{
	int height;

	int i;
	int j;



};
void merge(vector<G>& v, int low, int high);
void mergeSort(vector<G>& v, int low, int mid,int high);

int main(){


	ifstream fin;
	ofstream fout;
	vector<bool> finalstate;
	int casenum;
	fin.open("input.txt");
	fout.open("output.txt");

	

	fin>>casenum;

	for(int cn=0; cn<casenum;cn++)
	{
		G temp;
		bool state =true;
		int n,m,tempint;
		vector<G> glist,templist;
		
		vector<vector<G>> lawn;
		fin>>n>>m;

		
		for(int i=0; i<n; i++)
		{
			for(int j=0; j<m; j++)
			{
				fin>>tempint;
				temp.height = tempint;
				temp.i=i;
				temp.j=j;
				glist.push_back(temp);
				templist.push_back(temp);
			}
			lawn.push_back(templist);
			templist.clear();
			
		}


		merge(glist,0, glist.size()-1);

		for(int i=0; i<glist.size() &&state; i++)
		{
			bool jstate=true,istate=true;
			int gi, gj;
			gi=glist[i].i;
			gj=glist[i].j;
		
			
			for(int j=0; j<n &&istate; j++)
				if(lawn[j][gj].height>glist[i].height)
					istate =false;
			if(istate==false)
			{
				for(int j=0; j<m&& jstate; j++)
					if(lawn[gi][j].height>glist[i].height)
						jstate =false;
			}
			if(istate == false && jstate ==false) 
				state=false;
			
		}
		finalstate.push_back(state);

	
		lawn.clear();
		glist.clear();

	
	
	}



	for(int i=1; i<=casenum;i++)
	{
		fout<<"Case #"<<i<<": ";
		if(finalstate[i-1]==true)
			fout<<"YES"<<endl;
		else
			fout<<"NO"<<endl;
	}



}



void merge(vector<G>& v, int low, int high)
{
	if(low<high)
	{
		int mid=(high+low)/2;
		merge(v,low, mid);
		merge(v,mid+1, high);
		mergeSort(v,low, mid, high);
	

	}

}

void mergeSort(vector<G>& v, int low, int mid,int high)
{
 int h,i,j;
 vector<G> temp;
 h=low;
 j=mid+1;

 while((h<=mid)&&(j<=high))
 {
	 if(v[h].height>=v[j].height)
  {
	  temp.push_back(v[h]);
   h++;
  }
  else
  {
	  temp.push_back(v[j]);
   j++;
  }
  
 }
 if(h>mid)
 {
for(i=j;i<=high;i++)
  {
	  temp.push_back(v[i]);
  }
 }
 else
 {
	 for(i=h;i<=mid;i++)
	{
		temp.push_back(v[i]);
	}
 }
 for(i=0;i<temp.size();i++) 
	 v[i+low]=temp[i];
}

