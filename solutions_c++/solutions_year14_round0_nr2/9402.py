#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define BUFSIZE 1024

double recurfunc(double c, double f, double x, double nextincome, double prevtimetowin, double totaltime){
	double income = nextincome; // 0.2 cookies per 0.1s
	double incomeafterbuyfarm = 0.0;

	double curtime = 0.0;
	double timetobuyfarm = 0.0;
	double timeafterbuyfarm = 0.0;
	double totaltimetowin = 0.0;
	double aftertimetowin = 0.0;

	curtime = (x / income)/10.0;
	timetobuyfarm = (c / income)/10.0;

	incomeafterbuyfarm = income + f/10.0;
	timeafterbuyfarm = (x / incomeafterbuyfarm)/10.0;

	aftertimetowin = totaltime + timetobuyfarm + timeafterbuyfarm;


	if(prevtimetowin <= aftertimetowin){
		totaltime += curtime;
		return totaltime;
	}
	else if(prevtimetowin > aftertimetowin){
		totaltime += timetobuyfarm;
		income += f/10.0;
		return recurfunc(c, f, x, income, aftertimetowin, totaltime);
	}

}

void main()
{
	FILE *fin = NULL;
	FILE *fout = NULL;
	//fin = fopen("d:\\test\\sample.txt", "r");
	fin = fopen("d:\\test\\B-small-attempt0.in", "r");
	fout = fopen("d:\\test\\output.txt", "w");

	char buf[BUFSIZE] = {0,};
	char* find = NULL;
	int index = 1;

	int testcase = 0;
	double c = 0.0;
	double f = 0.0;
	double x = 0.0;
	double cookies = 0.0;
	
	int i = 0;


	char outbuf[BUFSIZE] = {0,};
	char temp[BUFSIZE] = {0,};

	char first[BUFSIZE] = {0,};
	char second[BUFSIZE] = {0,};
	char *p = NULL;
	int *pans = NULL;
	
	//√π¡Ÿ
	fgets(buf, BUFSIZE, fin);
	find = strchr(buf, 0x0A);
	if(find != NULL) *find = 0x00;
	
	testcase = atoi(buf);

	for(i=0; i<testcase; i++){
		fgets(buf, BUFSIZE, fin);
		find = strchr(buf, 0x0A);
		if(find != NULL) *find = 0x00;

		//c
		p = strtok(buf, " ");
		c = atof(p);
		
		//f
		p = strtok(NULL, " ");
		f = atof(p);

		//x
		p = strtok(NULL, " ");
		x = atof(p);

		double ret = recurfunc(c, f, x, 0.2, x/0.2/10, 0.0);
	


		printf("totaltime : %0.7f\n", ret);

		
		// file write
		strcpy(outbuf, "Case #");
		itoa(index, temp, 10);
		strcat(outbuf, temp);
		strcat(outbuf, ": ");

		sprintf(temp, "%0.7f", ret);
		strcat(outbuf, temp);
		strcat(outbuf, "\n");
		fwrite(outbuf, 1, strlen(outbuf), fout);
		index++;
	}


	fclose(fin);
	fclose(fout);
	return;
}