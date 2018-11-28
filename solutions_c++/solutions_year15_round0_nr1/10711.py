#include <stdio.h>

#define S_MAX 1001

#define S_MAX_entries 1001 * 9 

struct g_stack{
	int start_up_flag;
	int weight;
};

int main()
{
	struct g_stack G_STACK_ENTRIES[S_MAX_entries];
	//int G_STACK_ENTRIES[S_MAX_entries] = {0};
	int num_ins, weight, count, instr_len_toplus1, counter;

	int friends_to_invite, top, upto, standers;

	char instr[S_MAX];

	int stacktop, stck, stck2;

	FILE *fp;
	fp = fopen("A-small-attempt3.in","r"); // read mode

	FILE * fp1;
    fp1 = fopen ("A-small-attempt3.out", "w+");
	
	while(fscanf(fp, "%d", &num_ins) != EOF) {
		
		if(num_ins == 0) break;		

		for(count = 1; count <= num_ins; count++) {
		
			fscanf(fp, "%d %s", &instr_len_toplus1, instr);

			friends_to_invite = 0, top = 0;

			for(weight = 0; weight <= instr_len_toplus1; weight++) {

				//printf("%d ", instr[weight]-'0');
			
				if(instr[weight]-'0') {

					upto = instr[weight] - '0';

					counter = 1;

					if(weight == 0) {
					
						while(counter <= upto) {
							G_STACK_ENTRIES[top].start_up_flag = 1;
							G_STACK_ENTRIES[top].weight = weight;
							top++;
							counter++;
						}

					}				
					else if(weight) {						
					
						while(counter <= upto) {
							G_STACK_ENTRIES[top].start_up_flag = 0;
							G_STACK_ENTRIES[top].weight = weight;
							top++;
							counter++;
						}

					}
				
				}

			}

			stacktop = top;
			standers = 0;
			friends_to_invite = 0;
			/*
			for(stck = 0; stck < stacktop; stck++) {
				fprintf(fp1, "%d ", G_STACK_ENTRIES[stck].start_up_flag);
			}
			fprintf(fp1, "\n");
			for(stck = 0; stck < stacktop; stck++) {
				fprintf(fp1, "%d ", G_STACK_ENTRIES[stck].weight);
			}
			fprintf(fp1, "\n");
			*/
			for(stck = 0; stck < stacktop; stck++) {

				if(G_STACK_ENTRIES[stck].start_up_flag == 1) {
					standers ++;
					continue;
				}
			
				//if(G_STACK_ENTRIES[stck].start_up_flag == 0) {
				
					if(G_STACK_ENTRIES[stck].weight > standers) 
					{
						friends_to_invite += G_STACK_ENTRIES[stck].weight - standers;
						standers += friends_to_invite;
						standers++;
						//G_STACK_ENTRIES[stck].start_up_flag = 1; along with standers have flag start_up_flag = 1
					}
					else if(G_STACK_ENTRIES[stck].weight <= standers)
					{
						//G_STACK_ENTRIES[stck].start_up_flag = 1;
						standers++;
					}
				
				//}
			
			}

			//printf("\n");

			fprintf(fp1, "Case #%d: %d\n", count, friends_to_invite);
		}
	}
	
	return 0;
}
