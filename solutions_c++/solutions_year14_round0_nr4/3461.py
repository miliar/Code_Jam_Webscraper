#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
#include <fstream>
#include<iomanip>
using namespace std;
double findLargest(double array[],int n,bool change);
double lowestWeightGreater(double array[],int n,double item);
double findSmallest(double array[],int n,bool change);
void printArray(double array[],int n);
int main()
{
	int T,i,j,k,n,Ken_Points,Naomi_Points_War,Naomi_Points_Deceit;;
	double Naomi_chosen,Naomi_told,Ken_chosen;
	freopen("D-large.in","r",stdin);freopen("practice_large_out.out","w",stdout);
	cin>>T;
	for (int i = 0;i < T;i++)
    {   Ken_Points = 0;
		Naomi_Points_War = 0;
		Naomi_Points_Deceit = 0;
		cin>>n;
		double Naomi_Weights_War[n],Ken_Weights_War[n];
		double Naomi_Weights_Deceit[n],Ken_Weights_Deceit[n];
		for(j = 0;j < n;j++)
		cin>>Naomi_Weights_War[j];
		for(j = 0;j < n;j++)
		cin>>Ken_Weights_War[j];
		
		
		for(j = 0;j < n;j++)
		Naomi_Weights_Deceit[j] = Naomi_Weights_War[j];
		for(j = 0;j < n;j++)
		Ken_Weights_Deceit[j] = Ken_Weights_War[j];
		
		//War
		for(j = 0;j < n;j++)
		{
			Naomi_chosen = findLargest(Naomi_Weights_War,n,true);
			Ken_chosen = lowestWeightGreater(Ken_Weights_War,n,Naomi_chosen);
			if( Ken_chosen == -1.0)
			Ken_chosen = findSmallest(Ken_Weights_War,n,true);
			if (Naomi_chosen>Ken_chosen)
			Naomi_Points_War++;
		}
		//Deceitful War
		for(j = 0;j < n;j++)
		{
			Naomi_told = findLargest(Naomi_Weights_Deceit,n,false);
			if(Naomi_told > findLargest(Ken_Weights_Deceit,n,false))
		    {Ken_chosen = findSmallest(Ken_Weights_Deceit,n,true);
			Naomi_chosen = lowestWeightGreater(Naomi_Weights_Deceit,n,Ken_chosen);
		    }
			else
	     	{
			Ken_chosen = findLargest(Ken_Weights_Deceit, n,true);
		   	Naomi_chosen = findSmallest(Naomi_Weights_Deceit,n,true);
			}
			if(Naomi_chosen>Ken_chosen)
	        Naomi_Points_Deceit++;
	       // cout<<Naomi_Points_Deceit<<endl;
           //printArray(Naomi_Weights_Deceit,n);
		   //	printArray(Ken_Weights_Deceit,n);
		}
		
		
		cout<<"Case #"<<i+1<<": "<<Naomi_Points_Deceit<<" "<<Naomi_Points_War<<" "<<endl;
	}
    return 0;
}
double findLargest(double array[],int n,bool change)
{
	 double largest = 0.0;
	 int i,val;
	 for(i=0;i<n;i++)
	 {
		   if(array[i]!= -1 && array[i] > largest)
		   {largest = array[i];
			val = i;
		    
		   }
	 }
	 if(change)
	 array[val]=-1.0;  //Replace the term by -1 if it is being used
	 return largest;
}
double findSmallest(double array[],int n,bool change)
{
	double smallest;
	int i,val;
	for(i = 0; i<n;i++)
{
	if(array[i]!=-1)
	{smallest = array[i];
	val = i;
	break;}
}
	for(i=0;i<n;i++)
{
	if(array[i]!=-1&&(array[i] < smallest))
     {
			smallest = array[i];
			val = i;
     }
}
if(change)
array[val] = -1.0;   //Replace the term by -1 if it is being used
return smallest;
}
double lowestWeightGreater(double array[],int n,double item)
{
   double lowest = -1.0;
   int i,val = -1;
   	for(i = 0; i<n;i++)
{
	if(array[i]!=-1 && array[i] > item)
	{lowest = array[i];
	val = i;
	break;
	}
}
   if(lowest != -1.0)
   {
       for(i = 0; i<n;i++)
	   {
	       if(array[i]!=-1)
		   {
		       if(array[i] > item && array[i] < lowest)
			   {
			       lowest = array[i];
			       val = i;
			   }
		   }
	   }
	   }
	   if(val!=-1)
	   array[val] = -1.0;    //Replace the term by -1 if it is being used
	  return lowest;
}
void printArray(double array[],int n)
{
	for(int i=0;i<n;i++)
     {
			cout<<array[i]<<" ";
     }
    cout<<endl;
}
