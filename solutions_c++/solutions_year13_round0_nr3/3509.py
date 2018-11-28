#!/bin/bash

function sqrt_infile {
    read n
    echo $n
    for ((i=0; $i<$n; i=$i+1)); do
        read a b
        # input to ./c should be ceil(sqrt(a)), floor(sqrt(b))
        sqa=$(echo "sqrt($a)" | bc)
        sqa2=$(echo "$sqa*$sqa" | bc)
        if [ "$sqa2" != "$a" ]; then
            sqa=$(echo "$sqa+1" | bc)
        fi
        sqb=$(echo "sqrt($b)" | bc)
        echo "$sqa $sqb"
    done
}

# sqrt A and B in all cases, then run ./c
sqrt_infile | ./c
