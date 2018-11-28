/* 
 * File:   main.cpp
 * Author: paulo
 *
 * Created on 4 de Maio de 2013, 12:00
 */

#include <stdio.h>
/*
 * 
 */

int solve(int *motes, int nmotes, int amys, int depth, int operations);

int solve(int *motes, int nmotes, int amys, int depth, int operations){
    if(depth >= nmotes)
        return operations;
    // If we can absorb, that's how we solve it!!
    if(amys > motes[depth])
        return solve(motes, nmotes, amys+motes[depth], depth+1, operations);
    // Here we do two things: either we skip the next one and proceed, 
    // just adding one operation, or we insert one, the largest that Amys 
    // can swallow. We don
    // If we can just remove
    int op_remove = solve(motes, nmotes, amys, depth+1, operations+1);
    if(amys==1)
        return op_remove;    
    int op_add = solve(motes, nmotes, amys*2-1, depth, operations+1);
    if(op_remove < op_add)
        return op_remove;
    else
        return op_add;
}

int main(int argc, char** argv) {
    
    int cases, current = 0;
    scanf("%d", &cases);
    int amys, nmotes, motes[100];
    while(current < cases){
        scanf("%d %d", &amys, &nmotes);
        for(int i=0;i<nmotes;i++)
            scanf("%d", &motes[i]);
        // Sorts the cases
        for(int i=0;i<nmotes-1;i++)
            for(int j=i+1;j<nmotes;j++)
                if(motes[i] > motes[j]){
                    int temp = motes[i];
                    motes[i]=motes[j];
                    motes[j]=temp;
                }
        // dumps the vector
        /*printf("Sorte Motes: ");
        for(int i=0;i<nmotes;i++){
            printf(" %d", motes[i]);
        }
        printf("\n");*/
        int operations = solve(motes, nmotes, amys, 0,0);
        printf("Case #%d: %d\n", current+1, operations);
        current++;
    }
    
    return 0;
}

