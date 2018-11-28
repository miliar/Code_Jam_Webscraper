

#include <iostream>
#include<iomanip>
#include<vector>
#include<algorithm>
using namespace std;

int removeFirstOcc(vector<char> &oMergedList,int iStart,int iEnd,char cCh){
	for(int i=iStart;i<=iEnd;i++){
		if(oMergedList[i]==cCh){
			oMergedList[i]=-1;
			return i;
		}
	}
	return -1;
}

int removeLastOcc(vector<char> &oMergedList,int iStart,int iEnd,char cCh){
	for(int i=iEnd;i>=iStart;i--){
		if(oMergedList[i]==cCh){
			oMergedList[i]=-1;
			return i;
		}
	}
	return -1;
}


void printvector(vector<double> iAr){
	cout<<"\nOutput:";
	for(int i=0;i<iAr.size();i++){
		cout<<iAr[i]<<" ";
	}
}

void mergeXY(vector<double> xList,vector<double> yList,vector<char> &output){
	int x=0,y=0,n=output.size(),l=xList.size();
	for(int i=0;i<n;i++){

		
		if(x<l && y<l){

			if(xList[x]<yList[y]){
				output[i]='X';
				x++;
			}
			else{
				output[i]='Y';
				y++;
			}
			continue;
		}
		if(x<l){
			for(;x<l;x++,i++){
				output[i]='X';
			}
		}
		else if(y<l){
			for(;y<l;y++,i++){
				output[i]='Y';
			}
		}
		
		
	}
	
}
/*
int getDecWarPoints(vector<char> mergedList){

	int xBuf,score,xStart;
	int low=0,n,ret;
	n=mergedList.size()-1;
	xBuf=0;
	score=0;
	xStart;
		for(int i=n;i>=low;i--){
			if(mergedList[i]=='X'){
				xBuf++;
				continue;
			}
			if(mergedList[i]=='Y'){
				if(xBuf>1){
					xBuf--;
					score++;
					continue;
				}
				xStart=removeFirstOcc (mergedList,xStart,i,'X')+1;
				
				if(xBuf==1){
					if(xStart<0){
						xBuf--;
						score++;
						continue;
					}
				}
				
				
			}

		}
	
	return score+xBuf;
}
*/

int getDecWarPoints(vector<double> X,vector<double> Y){
		int xStart,xEnd,yStart,yEnd,i;
		int n=X.size();
	int score=0;
		xStart=0;
	yStart=0;
	xEnd=X.size()-1;
	yEnd=Y.size()-1;
	for(int i=0;i<n;i++){
	
			if(X[xEnd]>Y[yEnd]){
				score++;	
					xEnd--;
			}
			else{
				xStart++;
			}
		yEnd--;
	}
	return score;
}
int getWarPoints(vector<char> mergedList){
		
	int yBuf,score,yStart;
	int low=0,n,maxScore;
	n=mergedList.size()-1;
	maxScore=mergedList.size()/2;
	yBuf=0;
	score=0;
	yStart;
		for(int i=n;i>=low;i--){
			if(mergedList[i]=='Y'){
				yBuf++;
				continue;
			}
			if(mergedList[i]=='X'){
				if(yBuf>0){
					yBuf--;
					score++;
					continue;
				}
				yStart=removeFirstOcc (mergedList,yStart,i,'Y')+1;

					if(yStart<0){
						break;
					}
				
				
			}

		}
	score=score;//+yBuf;
	return maxScore-score;
}
int main()
{
	vector<double> X;
	vector <double> Y;
	vector<char> mergedList;
	int iSize;
	int iCases;
	cin>>iCases;
	for(int round=0;round<iCases;round++){
	cin>>iSize;
	X.resize(iSize);
	Y.resize(iSize);
	mergedList.resize(iSize*2);
	for(int i=0;i<iSize;i++){
		cin>>X[i];
	}

	for(int i=0;i<iSize;i++){
		cin>>Y[i];
	}
		sort(X.begin(),X.end());
		sort(Y.begin(),Y.end());
		//printvector (X);
		//printvector (Y);
	mergeXY (X,Y,mergedList);
	cout<<"Case #"<<round+1<<": ";

	cout<<getDecWarPoints  (X,Y);
		cout<<" "<<getWarPoints (mergedList)<<"\n";
	}
	return 0;
}

