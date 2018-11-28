#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>


using namespace std;



int main(int argc, char* argv[])
{
	//ifstream fin ("C-large-2.in");
	ifstream fin ("B-small-attempt2.in");
    ofstream fout ("output.out");

	int cases;
	fin >> cases;

	cout<<cases<<endl;
	

	//(fin,buffer); //ignore first line

	for(int i=1;i<=cases;i++){
		fout << "Case #"<<i<<": ";

		int N,M;
		fin>>N;
		fin>>M;

		int **w=new int*[N];
		for(int k=0;k<N;k++)
			w[k] = new int[M];

		for(int x=0;x<N;x++)
			for(int y=0;y<M;y++)
				fin>>w[x][y];
		
		bool hor=false,vert=false;
		
		for(int x=0;x<N;x++){
			for(int y=0;y<M;y++){
				//vertical
				int it=0;
				while(it<N){
					if(w[x][y]<w[it++][y]){
						vert=true;
						//cout<<"x,y = "<<x<<","<<y<<endl;
						break;
					}

				}

				//horrizontal
				it=0;
				while(it<M){
					if(w[x][y]<w[x][it++]){
						hor=true;
						//cout<<"x,y = "<<x<<","<<y<<endl;
						break;
					}

				}

				if(hor && vert)
					break;

			}
			if(hor && vert)
				break;
			hor=false;vert=false;
		}
		if(hor && vert)
			fout<<"NO";
		else
			fout<<"YES";

		for(int k=0;k<N;k++)
			delete w[k];
		delete w;
		fout<<endl;
	}

	fin.close();
	fout.close();


	return 0;
}

