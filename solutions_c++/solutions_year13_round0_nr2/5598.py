//============================================================================
// Name        : Lawn.cpp
// Author      : Mostafa Shokrof
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>
using namespace std;

struct point{
	int x;
	int y;
	int len;
	point(int b,int a,int c)
	{
		x=a;
		y=b;
		len=c;
	}
};
bool compare_points( const point & e1, const point & e2)
{
	if(e1.len==e2.len)
	{
		if(e2.x==e1.x)
			return e1.y>e2.y;
		return e1.x>e2.x;
	}
	return e1.len<e2.len;
}
bool check_solution(int** target_map,int ** curr_map,vector<point> targets,int width,int height)
{
	if(targets.size()==0)//solution found
		return true;
	point curr_target=targets.back();
	//try horizontal solution
	//////////////////////////////make a new copy
	int **horz;
//	int **horz=new int*[height];
//	for(int i=0;i<height;i++)
//		horz=new int[width];
//	for(int i=0;i<height;i++)
//		for(int j=0;j<height;j++)
//		{
//			horz[i][j]=curr_map[i][j];
//		}
	vector<point> newtargets;
	for(int i=0;i<targets.size();i++)
	{
		newtargets.push_back(point(targets[i].y,targets[i].x,targets[i].len));
	}
	///////////////////////////////////////////
	bool canbe=true;
	for(int i=0;i<width;i++)
	{
		if(target_map[curr_target.y][i]<=curr_target.len)
		{
		//	horz[curr_target.y][i]=curr_target.len;
			if(target_map[curr_target.y][i]==curr_target.len)
			{
				for(int j=newtargets.size()-1;j>=0;j--)
				{
					if(newtargets[j].y==curr_target.y&&newtargets[j].x==i)
					{
						newtargets.erase(newtargets.begin()+j);
						break;
					}
				}
			}
		}
		else{
			canbe=false;
//			for(int p=0;p<height;p++)
//				delete [] horz[p];
//			delete [] horz;
			newtargets.clear();
			break;
		}
	}
	bool horiz_suceed=false;
	if(canbe)
	{
		horiz_suceed=check_solution(target_map,horz,newtargets,width,height);
	}
	//try vertical solution
	canbe=true;
	for(int i=0;i<height;i++)
		{
			if(target_map[i][curr_target.x]<=curr_target.len)
			{
			//	curr_map[i][curr_target.x]=curr_target.len;
				if(target_map[i][curr_target.x]==curr_target.len)
				{
					for(int j=targets.size()-1;j>=0;j--)
					{
						if(targets[j].y==i&&targets[j].x==curr_target.x){
							targets.erase(targets.begin()+j);
							break;
						}
					}
				}
			}
			else{
				canbe=false;
//				for(int p=0;p<height;p++)
//					delete [] curr_map[p];
//				delete [] curr_map;
				targets.clear();
				break;
			}
		}
		bool vert_suceed=false;
		if(canbe)
		{
			vert_suceed=check_solution(target_map,curr_map,targets,width,height);
		}
		return vert_suceed||horiz_suceed;

}
int main() {
	int notestcases;
	cin>>notestcases;
	for(int t=1;t<=notestcases;t++)
	{
		int width,height;
		cin>>height>>width;
		int** map_target=new int*[height];
		int** map_seed=new int*[height];
		vector<point> cut_targets;
		for(int i=0;i<height;i++)
		{
			map_target[i]=new int[width];
			map_seed[i]=new int[width];
		}
		for(int i=0;i<height;i++)
			for(int j=0;j<width;j++)
			{
				cin>>map_target[i][j];
				map_seed[i][j]=100;
				cut_targets.push_back(point(i,j,map_target[i][j]));
			}
		sort(cut_targets.begin(),cut_targets.end(),compare_points);
		bool sol=check_solution(map_target,map_seed,cut_targets,width,height);
		if(sol)
			printf("Case #%d: YES\n",t);
		else
			printf("Case #%d: NO\n",t);
	}
	return 0;
}
