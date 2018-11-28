/*input
100
0
1
2
11
77
32
194
3
116
105
64
94
185
10
113
83
166
47
67
34
49
95
73
107
132
158
84
89
182
124
20
74
96
5
110
85
69
189
68
15
8
163
183
7
40
62
76
112
150
75
128
171
149
86
155
33
44
198
125
165
199
79
147
142
63
24
181
81
53
200
129
82
30
184
52
108
173
80
54
48
152
191
6
164
25
170
51
78
126
12
127
13
65
136
9
42
22
145
4
175
*/
#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <string>


using namespace std;

int seenDigits[10];

void checkDigits(int num){
	char numChar[200];
	itoa(num, numChar, 10);
	int i = 0;
	while(numChar[i] != '\0'){
		seenDigits[numChar[i] - 48] = 1;
		i++;
	}
}

bool checkAllSeen(){
	int ret = 1;
	for(int i = 0; i < 10; i++){
		if(!seenDigits[i])
			ret = 0;
	}
	return ret;
}

int main(){
	int T, N;
	scanf("%d", &T);

	for(int t = 0; t < T; t++){

		scanf("%d", &N);
		printf("Case #%d: ", t+1);

		if(N == 0){
			printf("INSOMNIA\n");
			continue;
		}

		for(int i = 0; i < 10; i++){
			seenDigits[i] = 0;
		}
		
		int i = 0, num;
		while(!checkAllSeen()){
			i++;
			num = N * i;
			checkDigits(num);
		}
		printf("%d\n", i*N);
	}	



	return 0;
}