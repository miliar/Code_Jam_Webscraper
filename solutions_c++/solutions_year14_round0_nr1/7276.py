#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int t[4][4];
int t1[4];
int t2[4];
ifstream inputFile;
ofstream outputFile;
string s;
int* compare(int t1[4], int t2[4])
{
	int result[4];
	int e = 0;
	int c1;
	int c2;
	for(int i = 0; i< 4; i++)
	{
		c1 = t1[i];
		for(int j = 0; j < 4; j++)
		{
			c2 = t2[j];
			if(c1 == c2)
			{
				result[e] = c1;
				e++;
			}
		}
	}
	return result;
}

int check(int i, int j)
{
	if(i > 0 && j < 0)
		return i;
	else if(i < 0)
		return -1;
	else if(i > 0 && j > 0)
		return 0;
}

void work(int p) {
	
	int n1;
	int n2;
	const char *ss;
	getline(inputFile, s);
	ss = s.c_str();
	sscanf(ss,"%d",&n1);

	//scanf("%d", &n1);
	  
    for(int i=0; i<4; ++i) {
        //for (int j=0; j<4; ++j) {
            //scanf("%d", &t[i][j]);
		getline(inputFile, s);
		ss = s.c_str();
		sscanf(ss,"%d %d %d %d",&t[i][0],&t[i][1],&t[i][2],&t[i][3]);	
		
		if(i == n1-1)
			for(int j=0;j<4;j++)
				t1[j] = t[i][j]; 
        //}
    }
	
	getline(inputFile, s);
	ss = s.c_str();
	sscanf(ss,"%d",&n2);
	//scanf("%d", &n2);
	  
    for(int i=0; i<4; ++i) {
        //for (int j=0; j<4; ++j) {
            //scanf("%d", &t[i][j]);
		getline(inputFile, s);
		ss = s.c_str();
		sscanf(ss,"%d %d %d %d",&t[i][0],&t[i][1],&t[i][2],&t[i][3]);	
		if(i == n2-1)
			for(int j=0;j<4;j++)
				t2[j] = t[i][j]; 
        //}
    }
	int *c = compare(t1,t2);

	int r = check(c[0],c[1]);
	outputFile << "Case #" << p <<": ";
	printf("Case #%d: ", p);

    if (r>0) {
		outputFile << r << "\n";
        printf("%d\n", r);
    } else if (r==0){
		outputFile << "Bad magician!\n";
        printf("Bad magician!\n");
	} else {
	outputFile << "Volunteer cheated!\n";
		printf("Volunteer cheated!\n");
	}
    return;
}

int main() {
    int t; 
	int c = 1;
	inputFile.open("c:\\example.in",ios::in);
	outputFile.open("c:\\example.out", ios::out);
	//inputFile.read((char *) &t,1);
	getline(inputFile, s);
	const char *ss = s.c_str();
	sscanf(ss,"%d",&t);
	//scanf("%d", &t);
    while(t--) {
        work(c);
		c++;
    }
    return 0;
}

